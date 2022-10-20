from definitions import MNEMONICS
from utils import *

class Assembler:
    def __init__(
        self, 
        input_path="./assembly.txt", 
        start_index_memory=0, 
        output_path="./output/assembly_translated.txt"
    ):
        """
            Assembler mais simples que esse, impossível. Vou assumir que você fez o `.txt` direitinho, hein?
            Não vem falar caquinha se der ruim por aí.
            `input_path`: Caminho do arquivo .txt de entrada
            `start_index_memory`: Índice a partir do qual inicia a contagem das posições de cada instrução na memória
            `output_path`: Caminho do arquivo .txt de saída
        """
        self.input_path = input_path
        self.start_index_memory = start_index_memory
        self.output_path = output_path

    def translate(self):
        """
            Traduz o arquivo assembly para linguagem de máquina, utilizando
            os mnemônicos (usados como constantes no código `VHDL`)
        """
        index_counter = self.start_index_memory
        instruction = ""
        commands = []
        
        with open(file=self.input_path, mode="r", encoding="utf-8") as file_input:
            lines = file_input.readlines()
            for line in lines:
                line = line.strip("\n")
                line_splitted = line.split()

                instru_mnemonic = self.get_instruction_mnemonic(line_splitted)
                value = self.get_addr_or_immediate(line_splitted)
                comment = self.get_comment(line)

                if instru_mnemonic is not None:
                    instruction = f"tmp({index_counter})\t := " + instru_mnemonic
                    
                    if value is not None:
                        instruction += f' & "{value}";'
                    else:
                        instruction += f' & "000000000";'

                    if comment is not None:
                        instruction += f' -- {line_splitted[0]} {line_splitted[1]}  {comment}'

                    commands.append(instruction)
                    index_counter += 1
        
        with open(file=self.output_path, mode="w", encoding="utf-8") as file_output:
            for command in commands:
                file_output.write(command)
                file_output.write("\n") 


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


    def get_addr_or_immediate(self, line_splitted):
        """
            Retorna valor do imediato ou endereço em binário
            `line`: linha de instrução assembly 
        """
        if (line_splitted.__len__() > 1) and (("@" in line_splitted[1]) or ("$" in line_splitted[1])):
            return get_binary_from_int(int(line_splitted[1][1:]), 9)
        else:
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
            

my_assemb = Assembler()
my_assemb.translate()