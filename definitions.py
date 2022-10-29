# Mnemônicos e seus respectivos opcodes em binário
# de 4 dígitos
MNEMONICS = {
    "NOP" : "0000",
    "LDA" : "0001",
    "SOMA": "0010",
    "SUB" : "0011",
    "LDI" : "0100",
    "STA" : "0101",
    "JMP" : "0110",
    "JEQ" : "0111",
    "CEQ" : "1000",
    "JSR" : "1001",
    "RET" : "1010",
    "ANDOP" : "1011",
}

JMPS = ["JMP", "JSR", "JEQ"]

REGS = {
    "R0": "00",
    "R1": "01",
    "R2": "10",
    "R3": "11",
}
