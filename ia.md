# Bitácora de Prompts e Interacción con IA

## Prompt 1: Generación de Plantillas HTML Base
- **Contexto:** Error `TemplateDoesNotExist` al intentar acceder a la ruta `/login/`.
- **Instrucción:** Crear la estructura y código base para las plantillas `login.html`, `lista.html`, `form.html` y `confirmar.html` en la app `core`.
- **Resultado:** Archivos HTML funcionales con estilos CSS nativos embebidos para permitir autenticación, listado de registros, formulario de creación/edición y confirmación de eliminación.

## Prompt 2: Rediseño Visual a Tema Oscuro Moderno
- **Contexto:** Necesidad de mejorar la interfaz con una estética sobria, moderna y elegante.
- **Instrucción:** Aplicar un diseño Dark/Slate Moderno con colores oscuros (#0f172a, #1e293b), bordes suavemente redondeados, tipografía limpia y componentes interactivos (badges, botones con hover).
- **Resultado:** Actualización completa del CSS embebido en todas las plantillas HTML para mantener cohesión gráfica.

## Prompt 3: Lógica Condicional de Colores para Estado y Resultado
- **Contexto:** La vista de listado no diferenciaba visualmente los estados de aprobación mediante colores de alto contraste.
- **Instrucción:** Modificar la lógica en `lista.html` usando filtros Jinja/Django (`|lower` e `in`) para que las cadenas que contengan "aprobado" o "aceptado" se muestren en badge verde (`.badge-aceptado`), y las de rechazo en badge rojo (`.badge-rechazado`). Correcto renderizado de la columna "Estado" (Aceptado/Rechazado) y "Resultado".
- **Resultado:** Visualización clara e intuitiva sin necesidad de lectura exhaustiva del texto.