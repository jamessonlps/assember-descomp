from definitions import MNEMONICS, REGS, JMPS
from utils import *

class Assembler:
    def __init__(
        self, 
        input_path="./assembly.txt", 
        start_index_memory=0, 
        output_path="./output/assembly_translated.txt"
    ):
        """
            Seguir o modelo do arquivo `assembly.txt` para escrever as instruções
            `input_path`: Caminho do arquivo .txt de entrada
            `start_index_memory`: Índice a partir do qual inicia a contagem das posições de cada instrução na memória
            `output_path`: Caminho do arquivo .txt de saída
        """
        self.input_path = input_path
        self.start_index_memory = start_index_memory
        self.output_path = output_path
        self.labels_addrs = {}


    def translate(self):
        """
            Traduz o arquivo assembly para linguagem de máquina, utilizando
            os mnemônicos (usados como constantes no código `VHDL`)
        """
        index_counter = self.start_index_memory
        instruction = ""
        commands = []
        
        with open(file=self.input_path, mode="r", encoding="utf-8") as file_input:
            self.get_labels_addresses()
            lines = file_input.readlines()
            for line in lines:
                line = line.strip("\n")
                line_splitted = line.split()

                instru_mnemonic = self.get_instruction_mnemonic(line_splitted)
                # value = self.get_addr_or_immediate(line)
                reg, address = self.get_addr_or_immediate(line)
                comment = self.get_comment(line)

                if instru_mnemonic is not None:
                    instruction = f"tmp({index_counter})\t := " + instru_mnemonic

                    # Se não houver registrador especificado, passa o R0
                    if reg is not None:
                        instruction += f' & {reg}'
                    else:
                        instruction += f' & R0'
                    
                    # Se não houver endereço, usa "000000000"
                    if address is not None:
                        instruction += f' & "{address}";'
                    else:
                        instruction += f' & "000000000";'

                    # Usa comentário, se houver
                    if comment is not None:
                        instruction += f' -- {comment}'

                    commands.append(instruction)
                    index_counter += 1
        
        with open(file=self.output_path, mode="w", encoding="utf-8") as file_output:
            for command in commands:
                file_output.write(command)
                file_output.write("\n") 


    def get_labels_addresses(self):
        pc_counter = 0
        with open(file=self.input_path, mode="r", encoding="utf-8") as file_input:
            lines = file_input.readlines()
            for line in lines:
                if line.startswith(":"):
                    label = line[1:-1]
                    self.labels_addrs[label] = pc_counter
                else:
                    pc_counter+=1


    def get_instruction_mnemonic(self, line_splitted):
        """
            Retorna o opcode de 4 bits referente a instrução da linha
            `line`: linha de instrução assembly 
        """
        try:
            if line_splitted[0].upper() in MNEMONICS.keys():
                return line_splitted[0].upper()
            return None
        except:
            return None


    def get_addr_or_immediate(self, line: str):
        """
            Retorna valor do imediato ou endereço em binário
            `line`: linha de instrução assembly 
        """
        line_splitted = line.split()
        reg = None
        address = None

        # Instruções NOP e labels
        if len(line_splitted) == 1:
            return reg, address
        
        value1 = line_splitted[1]
        
        if ("@" in value1):
            address = get_binary_from_int(self.labels_addrs[value1[1:]], 9)
        else:
            if value1.upper() in REGS.keys():
                reg = value1.upper()

        if len(line_splitted) > 2:
            value2 = line_splitted[2]
            if ("@" in value2) or ("$" in value2):
                address = get_binary_from_int(int(value2[1:]))

        return reg, address


    def get_register(self, line_splitted):
        """
            Retorna o registrador utilizado na operação
            `line_splitted`: array de strings da linha de instrução assembly
        """
        if (line_splitted.__len__() > 1):
            reg = line_splitted[1][:]
            try:
                if reg in REGS.keys():
                    return reg
                else:
                    return None
            except:
                return None


    def get_comment(self, line: str):
        """
            Retorna o comentário na instrução Assembly, se existir
            `line`: linha de instrução assembly 
        """
        if "#" in line:
            line_splitted = line.split(sep="#")
            return line_splitted[-1]
        else:
            return None
            

my_assemb = Assembler(input_path='./teste.txt', output_path='./output/teste.txt')
my_assemb.translate()