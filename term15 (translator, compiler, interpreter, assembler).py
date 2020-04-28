# Translator, compiler, intrepreter, assembler

# why should we use them?
# we are mostly code in high level languages in computers.
# but computer processor only understand machine language (low level language) not human readable (high level language).
# for computer every code must be in 0 and 1 form, called binary.
# so our language must be converted from high level to low level so that our processor could understand that.

# by the way, language are 2 types.
# low level and high level.
# they are also a middle level for C. because C is both low and high level language.

# low level is machine dependent.
# high level is understandable by humans/users.

# Translator
# It is a converter which converts source languge to destination language.
# It provides an interface to computer, to read high level language code.
# here the source language is a high level language and destination language is the low level language.
# it is generally a software program.
# it entirely depends on languages.
# Translator are of 3 types:
    # 1. Compiler
    # 2. Assembler
    # 3. Intrepreter


# Compiler
# read the high level code and change it to low level/ Machine code.
# it turns a program firstly in a executable with debugging that.
# after execution user input data and then the executable execute and return the output.

# so in general compiler takes the source code(.C/.CPP),
# then turns it to Object code (.OBJ),
# then turns it to a executable file (.EXE)
# then we can input in the exe file and get the output.

# compilers work on a whole page at a single time.
# converts whole page into object code.
# the object code is a machine code that the processor can execute one instruction at a time.
# compiler belongs to 3rd generation language (3GL).
# exp. Boreland, GCC, Turbo C, Turbo C++, Just in time.


# Interpreter
# reads the high level language and converts it to low level language.

# it takes the program and the input data "in the same time".
# the it interepret them and gives us the output.

# it is a computer program that directly executes instructions written is a programming language or scripting language
# without previously compiling them into a machine language program.
# it works or perform operations line by line.
# it produce output together with program execution.
# generally uses following strategy:
    # translate source code into some efficient intermediate representation and immidiately execute this.
# exp.
    # Java VM - runs java byte code.

# Differnce between Compiler and Interpreter:
# The main difference is that 
# an interpreter directly executes the instructions in the source programming language 
# while a compiler translates those instructions into efficient machine code.
# An interpreter will typically generate an efficient intermediate representation and immediately evaluate it.

# Which is Faster?
# A compiled program is faster to run than an interpreted program,  
# but it takes more time to compile and run a program than to just interpret it. 
# A compiler indeed produces faster programs. 
# It happens fundamentally because it must analyze each statement just once,
# while an interpreter must analyze it each time.

# In short, Compiler executes conditional control statements (like if-else and switch-case) and logical constructs faster than interpreter.
# Interpreter execute conditional control statements at a much slower speed.
# Compiled programs take more memory because the entire object code has to reside in memory.

# An Interpreter directly executes instructions written in a programming or scripting language 
# without previously converting them to an object code or machine code. 
# Examples of interpreted languages are Perl, Python and Matlab.

# An interpreter translates high-level instructions into an intermediate form, which it then executes.
# In contrast, a compiler translates high-level instructions directly into machine language. 
# Compiled programs generally run faster than interpreted programs.
# This process can be time-consuming if the program is long.

# Is python a compiled language or interpreted language?
# There are multiple implementations of Python language .  
# The official one is a byte code interpreted one.
# There are byte code JIT compiled implementations too.
# As concluding remarks, Python(Cpython) is neither a true compiled time nor pure interpreted language
# but it is called interpreted language.

# Assemblers
# it is dedicated for only assembly languages.
# read the assembly level code and convert it to machine code.

# An assembler is a type of computer program that interprets software programs written in assembly language into machine language,
# code and instructions that can be executed by a computer.
 
# the code and operators in assembly language called "mnemonics".
# assembler read mnemonics and converts into machine dependent language directly.
# an assembler enables software and application developers to access, operate and manage a computers hardware architecture and components.
# assembler directly interects with the hardware.
# an assembler is sometimes referred to as the compiler of assembly language.
# it also provides the services of an interpreter.
# it means it read the whole page at a time and also it provides services like interpreter
# an assembler works by assembling and converting the source code of assembly language into object code or
# an object file (which constitutes a stream of zeroes and ones of machine code),
# which are directly executable by the processor.

# what is Cython?
# Cython is a programming language that aims to be a superset of the Python programming language,
# designed to give C-like performance with code 
# that is written mostly in Python with optional additional C-inspired syntax.
# Cython is a compiled language that is typically used to generate CPython extension modules
