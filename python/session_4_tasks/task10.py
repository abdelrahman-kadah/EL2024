"""
Class Generator
"""

className = input("Enter the class name: ")
classNamespace = input("Enter the class namespace: ")

with open(f"{className}.hpp", "w") as f:
    f.write(f"#ifndef {className.upper()}_HPP\n\
#define {className.upper()}_HPP\n\n\
namespace {classNamespace} {{\n\n\
class {className.capitalize()} {{\n\
public: \n \
    {className.capitalize()}();\n\
    ~{className.capitalize()}();\n\
}};\n \
}}\n \
#endif")


with open(f"{className}.cpp", "w") as f:
    f.write(f"""#include "{className.capitalize()}.hpp" \n\n\n\
            
namespace {classNamespace} {{ \n\n\n\

{className.capitalize()}::{className.capitalize()}()  {{}} \

{className.capitalize()}::~{className.capitalize()}() {{}} \

}}

""") 

    