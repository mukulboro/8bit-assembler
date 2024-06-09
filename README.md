# 8 Bit Assembler
Assembler that takes in a custom instruction set to generate RAM image to be used in Logisim.

## What is this?
This script is was written for my team's Computer Organization & Architecture project where we designed and simulated an 8 bit CPU.  
The script takes in code written in a custom assembly instruction set and generates RAM Image that can be loaded onto Logisim.

## Instruction Set

| Opcode | Operand? | BINARY   |
|--------|----------|---|
| LOADA  | YES      | 00010 |  
| LOADB  | YES      | 0001| 
| ADD    | NO       | 0010 | 
| STORE    | YES       | 0011 | 

## Usage
```
python3 . -h
```

## Example

- Code:
```
INIT e=5
LOADA f
LOADB e
ADD
STORE f
```
- Explanation: 
This code is used to count with increments of 5.
    - Initialize memory location "e" with value 5.
    - Load value at memory lococation "f" onto register A.
    - Load value at memory lococation "e" onto register B.
    - Add the contents of register A and B.
    - Store contents of output regsiter to memory location "f".
- Assembler Output
```
v2.0 raw
0f 1e 20 3f 00 00 00 00 00 00 00 00 00 00 5 00
```
