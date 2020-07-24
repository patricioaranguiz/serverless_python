#Servicios lambdas con la configuración de S3

Conjunto de servicios Lambdas creados con el Framework Serverless el lenguaje Python. 

#### _Configuración_
Configurar tus credenciales con **Serverless Framework**.  
Crear un Rol en **IAM** de **AWS** con permisos sobre **S3** (en el caso de estas pruebas se utilizó acceso completo).  

Una vez realizado lo anterior debe agregar en el archivo **env.yml**

**ROLE**: Debe ser el rol creado en el IAM (arn:aws:iam::).  
**BUCKET_NAME**: Nombre del bucket que tu quieras