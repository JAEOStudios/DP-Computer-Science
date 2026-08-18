"""
A1-2-fde-trace.py  --  Lesson A1-2: The Fetch, Decode, Execute Cycle
DP Computer Science, Topic A1: Computer Fundamentals

A paced walkthrough of the cycle. It stops after every stage and waits for you,
so you can predict what moves next before it happens.

It runs the same four-instruction program you will type into the Little Man
Computer later in the lesson, and the same one that appears in Q6 of your
Guided Notes. Registers are named the way the syllabus names them because the LMC organizes things
slightly differently.

Run it:   python A1-2-fde-trace.py
Controls: [Enter] advances one stage,  a = run the rest automatically,  q = quit
"""

import time

# ---------------------------------------------------------------------------
# MEMORY  -  the addresses match what LMC assigns when you assemble the program
# ---------------------------------------------------------------------------
memory = {
    0: 'LDA 4',  # load the contents of address 4 into the accumulator
    1: 'ADD 5',  # add the contents of address 5 to the accumulator
    2: 'STA 6',  # store the accumulator into address 6
    3: 'HLT',  # stop
    4: '12',  # NUM1
    5: '30',  # NUM2
    6: '0',  # RESULT
}
LABELS = {4: 'NUM1', 5: 'NUM2', 6: 'RESULT'}

reg = {'PC': '0', 'MAR': '-', 'MDR': '-', 'IR': '-', 'AC': '0'}
bus = {'ADDRESS': '', 'DATA': '', 'CONTROL': ''}

auto = False
cycle = 0


def panel(stage, changed, note):
    """Redraw the whole machine. Plain text only - no escape codes, so this
    behaves itself inside the PyCharm run window."""
    global auto
    print('\n' * 2)
    print('=' * 70)
    print((' CYCLE %d' % cycle).ljust(48) + ('stage: %s' % stage).rjust(22))
    print('=' * 70)
    print()

    # ---- left block: the CPU ------------------------------------------------
    left = ['  CPU', '  +----------------------+']
    for name in ('PC', 'MAR', 'MDR', 'IR', 'AC'):
        mark = '<--' if name == changed else '   '
        left.append('  | %-4s %-11s %s |' % (name, reg[name], mark))
    left.append('  +----------------------+')

    # ---- right block: memory ------------------------------------------------
    right = ['MEMORY', '+-----+----------+---------+']
    for addr in sorted(memory):
        right.append('| %3s | %-8s | %-7s |' % (addr, memory[addr], LABELS.get(addr, '')))
    right.append('+-----+----------+---------+')

    width = max(len(x) for x in left) + 6
    for i in range(max(len(left), len(right))):
        a = left[i] if i < len(left) else ''
        b = right[i] if i < len(right) else ''
        print(a.ljust(width) + b)

    print()
    for b in ('ADDRESS', 'DATA', 'CONTROL'):
        content = bus[b] if bus[b] else '.' * 10
        print('   %-13s [ %s ]' % (b + ' BUS', content.center(16)))
    print()

    # wrap the commentary at 68 columns so it never runs off a projector
    words, line = note.split(), ' >'
    for w in words:
        if len(line) + len(w) + 1 > 68:
            print(line);
            line = '   '
        line += ' ' + w
    print(line)
    print()

    if auto:
        time.sleep(1.4)
        return
    try:
        choice = input(' [Enter] next   a = auto   q = quit  > ').strip().lower()
    except EOFError:
        auto = True
        return
    if choice == 'q':
        raise SystemExit('\nStopped.\n')
    if choice == 'a':
        auto = True


def clear_buses():
    for b in bus:
        bus[b] = ''


print(__doc__)
try:
    input(' [Enter] to start ')
except EOFError:
    auto = True

running = True
while running:
    cycle += 1

    # ------------------------------ FETCH ----------------------------------
    clear_buses()
    reg['MAR'] = reg['PC']
    panel('FETCH 1', 'MAR',
          'The address in the PC is copied into the MAR. This is internal to '
          'the CPU - nothing is on any bus yet.')

    bus['ADDRESS'] = reg['MAR']
    panel('FETCH 2', None,
          'The MAR puts that address onto the ADDRESS bus. One direction only: '
          'CPU to memory.')

    bus['CONTROL'] = 'READ'
    panel('FETCH 3', None,
          'The control unit asserts READ on the CONTROL bus. Memory now knows '
          'this is a read, not a write.')

    fetched = memory[int(reg['MAR'])]
    bus['DATA'] = fetched
    reg['MDR'] = fetched
    panel('FETCH 4', 'MDR',
          'Memory copies its contents onto the DATA bus and it lands in the '
          'MDR. Note that memory still holds it - a read copies, it does not move.')

    reg['IR'] = reg['MDR']
    clear_buses()
    panel('FETCH 5', 'IR',
          'The instruction moves from the MDR into the IR. The MDR is only ever '
          'a staging post.')

    reg['PC'] = str(int(reg['PC']) + 1)
    panel('FETCH 6', 'PC',
          'The PC is incremented NOW, during fetch - not after execute. The CPU '
          'already knows where it is going next.')

    # ------------------------------ DECODE ---------------------------------
    parts = reg['IR'].split()
    opcode = parts[0]
    operand = int(parts[1]) if len(parts) > 1 else None
    panel('DECODE', None,
          f'The control unit reads the opcode "{opcode}" out of the IR' +
          (f' and sees it needs the contents of address {operand}.'
           if operand is not None else ' and sees it needs no operand.'))

    # ------------------------------ EXECUTE --------------------------------
    if opcode == 'LDA':
        reg['MAR'] = str(operand)
        bus['ADDRESS'] = str(operand)
        bus['CONTROL'] = 'READ'
        reg['MDR'] = memory[operand]
        bus['DATA'] = memory[operand]
        reg['AC'] = reg['MDR']
        panel('EXECUTE', 'AC',
              f'Address {operand} goes out on the ADDRESS bus, READ on the '
              f'CONTROL bus, and {memory[operand]} comes back on the DATA bus '
              f'into the accumulator.')

    elif opcode == 'ADD':
        reg['MAR'] = str(operand)
        bus['ADDRESS'] = str(operand)
        bus['CONTROL'] = 'READ'
        reg['MDR'] = memory[operand]
        bus['DATA'] = memory[operand]
        reg['AC'] = str(int(reg['AC']) + int(reg['MDR']))
        panel('EXECUTE', 'AC',
              f'{memory[operand]} is fetched the same way, and the ALU adds it '
              f'to the accumulator. AC is now {reg["AC"]}.')

    elif opcode == 'STA':
        reg['MAR'] = str(operand)
        reg['MDR'] = reg['AC']
        bus['ADDRESS'] = str(operand)
        bus['CONTROL'] = 'WRITE'
        bus['DATA'] = reg['AC']
        memory[operand] = reg['AC']
        panel('EXECUTE', 'MDR',
              f'This time the CONTROL bus says WRITE, and the DATA bus runs the '
              f'other way. Address {operand} now holds {reg["AC"]}.')

    elif opcode == 'HLT':
        clear_buses()
        panel('EXECUTE', None,
              'HLT. The control unit stops the clock. Nothing on any bus, and '
              'nothing more will happen until the machine is reset.')
        running = False

print('=' * 68)
print(f' Finished after {cycle} cycles.')
print(f' Accumulator = {reg["AC"]}')
print(f' RESULT (address 6) holds {memory[6]} - it started at 0.')
print()
print(' Now compare that against your Q6 trace table, then type the same')
print(' program into LMC and watch the PC and ACC do exactly the same thing.')
print('=' * 68)