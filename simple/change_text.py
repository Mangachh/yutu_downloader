

def up_and_down(text: str) -> str:
    upper = True
    final = ""
    for c in text:
        if upper:
            final += c.capitalize()
        else:
            final += c.lower()
        
        upper = not upper
           
            
    return final

if __name__ == "__main__":
    text = input("Escribe un text: ")
    text = up_and_down(text)
    print(f"Texto en versión cani:\n{text}")