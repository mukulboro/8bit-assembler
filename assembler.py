import sys

CONFIG_FILE_NAME = "config"
CODE_FILE_NAME = "multiples5.a"
OUTPUT_FILE_NAME = "program"
HEADER = "v2.0 raw"

class Assembler:
    def __init__(self, cfg_file:str, code_file:str, op_file="program", header="v2.0 raw"):
        self.cfg = cfg_file
        self.code = code_file
        self.op= op_file
        self.header = header
        self.final_data = str()
        
    def _parse_cfg(self):
        with open(self.cfg, "r") as f:
            cfg = f.readlines()
        config = dict()
        try:
            for c in cfg:
                opcode, instuction_code = c.split(" ")
                config[opcode] = int(instuction_code.strip())
            
            return config
        except BaseException as e:
            raise Exception("Invalid configuration format")    
        
    def _open_file(self):
        with open(self.code, "r") as f:
            code = f.readlines()
        if not (code[0].split(" "))[0]=="INIT": # Initialization params are required
            raise Exception("Invalid initialization")
        # Init can only have 8 data
        init_data = (code[0].split(" ")[1:])[0].split(",")
        if(len(init_data)>8):
            raise Exception("Too many Initialization Parameters")
        
        clean_init_data = [x.strip() for x in init_data]
        other_lines = code[1:]
        if(len(other_lines)>8): # Only 8 instructions are permitted
            raise Exception("Too many instructions. Can't fit on RAM")
        
        clean_instructions = [x.strip() for x in other_lines]
        
        return clean_init_data, clean_instructions
    
    def _parse_instructions(self, instructions, cfg):
        opcodes = list(cfg.keys())
        output = ["00"]*8
        try:
            for idx, op in enumerate(instructions):
                operation = op.split(" ")
                if operation[0] not in opcodes:
                    raise Exception(f"Invalid opcode {op}")
                if not operation[0] == "ADD":
                    address = operation[1] 
                    address_hex = int(f"0x{address}", 16)
                    if address_hex < 7 and address_hex > 0x0f:
                        raise Exception("Invalid range for memory address")
                    opcode_hex = opcodes.index(operation[0])
                    ram_string = f"{opcode_hex}{address}"
                    output[idx] = ram_string
                else:
                    output[idx] = "20"
            return output
        except BaseException as e:
            raise Exception("Invalid code format")
    
    def _parse_init(self, init_data):
        output = ["00"]*16
        try:
            for idx, i in enumerate(init_data):
                location, data = i.split("=")
                data_hex = int(f"0x{data}", 16)
                if data_hex > 0xff:
                    raise BaseException("Data word greater than 8 bit")
                location_hex = int(f"0x{location}", 16)
                if location_hex > 0xf or location_hex < 7:
                    raise BaseException("Invalid address")
                output[location_hex] = data
            return output
        except BaseException as e:
            raise Exception("Invalid Initialization")
        
    def compile(self):
        complied_list = ["00"]*16
        config = self._parse_cfg()
        init_data, instructions = self._open_file()
        instruction_list = self._parse_instructions(instructions, config)
        init_list = self._parse_init(init_data)
        for idx, i in enumerate(init_list):
            complied_list[idx] = init_list[idx]
        for idx, i in enumerate(instruction_list):
            complied_list[idx] = instruction_list[idx]
        compiled_string = " ".join(complied_list)
        with open(self.op, "w") as f:
            f.writelines([self.header, "\n" , compiled_string])
        

a = Assembler(cfg_file=CONFIG_FILE_NAME, code_file=CODE_FILE_NAME, op_file=OUTPUT_FILE_NAME, header=HEADER)
a.compile()