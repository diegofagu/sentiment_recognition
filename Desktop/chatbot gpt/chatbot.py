
# Importar los módulos necesarios
# Asegúrese de que estos módulos estén instalados y sean accesibles en su entorno de Python
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# Crear una instancia del modelo
model = ChatOpenAI(model="gpt-4o")

# Definir system_prop
system_prop = "alguna_propiedad_del_sistema"

# Crear el mensaje
message = {
    SystemMessage(system_prop),
    HumanMessage("Como preparo una cazuela")
}

# Invocar el modelo con el mensaje
result = model.invoke(message)

# Imprimir el contenido del resultado
print(result.content)