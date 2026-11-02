# app.py  —  CLASES 6 y 7
# Frontend con Streamlit. Se ejecuta con:   streamlit run app.py
# La estructura ya está hecha. Completá los TODO.
import streamlit as st

from modelos import Producto, Proyecto
from almacenamiento import guardar, cargar
from estadisticas import resumen
from graficos import graficar

st.set_page_config(page_title="Gestor de proyectos", layout="wide")
st.title("Gestor de proyectos y productos")

# --- Datos: se cargan una sola vez y se guardan en st.session_state ---
# (Streamlit vuelve a ejecutar todo el archivo en cada click; session_state
#  es la "memoria" que se mantiene entre ejecuciones.)
if "proyectos" not in st.session_state:
    st.session_state.proyectos = cargar()
proyectos = st.session_state.proyectos

# --- Barra lateral: elegir o crear proyecto ---
st.sidebar.header("Proyectos")

nuevo_nombre = st.sidebar.text_input("Nombre del nuevo proyecto")
if st.sidebar.button("Crear proyecto"):
    existentes = [p.nombre for p in proyectos]
    if nuevo_nombre.strip() == "":
        st.sidebar.error("Escribí un nombre")
    elif nuevo_nombre.strip() in existentes:
        st.sidebar.error("Ya existe un proyecto con ese nombre")
    else:
        proyectos.append(Proyecto(nuevo_nombre.strip()))
        guardar(proyectos)
        st.sidebar.success("Proyecto creado")

if len(proyectos) == 0:
    st.info("Creá tu primer proyecto desde la barra lateral.")
    st.stop()

nombres_proyectos = [p.nombre for p in proyectos]
elegido = st.sidebar.selectbox("Proyecto actual", nombres_proyectos)
proyecto = proyectos[nombres_proyectos.index(elegido)]

st.subheader(f"Proyecto: {proyecto.nombre}")
tab_productos, tab_graficos, tab_resumen = st.tabs(["Productos", "Gráficos", "Resumen"])

# --- Pestaña 1: productos ---
with tab_productos:
    st.markdown("#### Agregar producto")
    with st.form("form_producto", clear_on_submit=True):
        nombre = st.text_input("Nombre")
        col1, col2, col3, col4 = st.columns(4)
        stock = col1.number_input("Stock", min_value=0, step=1)
        costo = col2.number_input("Costo", min_value=0.0, step=1.0)
        precio = col3.number_input("Precio de venta", min_value=0.0, step=1.0)
        ventas = col4.number_input("Ventas (unidades)", min_value=0, step=1)

        # DESAFÍO FINAL (extra): agregar acá dos campos para que el usuario
        # invente una propiedad (nombre + valor) y guardarla en el diccionario "extras".

        enviado = st.form_submit_button("Agregar producto")

    if enviado:
        if nombre.strip() == "":
            st.error("El producto necesita un nombre")
        else:
            # TODO 1: crear el Producto con los datos del formulario
            # y agregarlo con proyecto.agregar_producto(...).
            # Si se pudo: guardar(proyectos) y st.success("Producto agregado")
            # Si no (nombre repetido): st.error("Ya existe un producto con ese nombre")
            pass

    st.markdown("#### Productos del proyecto")
    if len(proyecto.productos) == 0:
        st.info("Todavía no hay productos.")
    else:
        # TODO 2: armar una lista "filas" con un diccionario por producto:
        #   fila = {"nombre": p.nombre}
        #   fila.update(p.propiedades())
        # y mostrarla con st.dataframe(filas)
        pass

        st.markdown("#### Editar producto")
        a_editar = st.selectbox("Producto a editar", proyecto.nombres_productos(), key="editar")
        actual = proyecto.buscar(a_editar)
        # La key incluye el nombre del producto para que los campos se actualicen al cambiar de producto
        with st.form("form_editar"):
            c1, c2, c3, c4 = st.columns(4)
            nuevo_stock = c1.number_input("Stock", min_value=0, step=1, value=int(actual.stock), key=f"stock_{a_editar}")
            nuevo_costo = c2.number_input("Costo", min_value=0.0, step=1.0, value=float(actual.costo), key=f"costo_{a_editar}")
            nuevo_precio = c3.number_input("Precio de venta", min_value=0.0, step=1.0, value=float(actual.precio), key=f"precio_{a_editar}")
            nuevas_ventas = c4.number_input("Ventas (unidades)", min_value=0, step=1, value=int(actual.ventas), key=f"ventas_{a_editar}")
            guardar_cambios = st.form_submit_button("Guardar cambios")

        if guardar_cambios:
            # TODO 6: llamar a proyecto.editar_producto(...) con los valores nuevos,
            # guardar(proyectos), mostrar st.toast("Producto actualizado") y volver a dibujar con st.rerun()
            pass

        st.markdown("#### Eliminar producto")
        a_borrar = st.selectbox("Producto", proyecto.nombres_productos(), key="borrar")
        if st.button("Eliminar"):
            # TODO 3: eliminar el producto, guardar y volver a dibujar con st.rerun()
            pass

# --- Pestaña 2: gráficos ---
with tab_graficos:
    if len(proyecto.productos) == 0:
        st.info("Agregá productos para ver gráficos.")
    else:
        todos = proyecto.nombres_productos()
        props = proyecto.nombres_propiedades()
        productos_elegidos = st.multiselect("Productos", todos, default=todos)
        props_elegidas = st.multiselect("Propiedades", props, default=["ventas"])

        if len(productos_elegidos) == 0 or len(props_elegidas) == 0:
            st.warning("Elegí al menos un producto y una propiedad.")
        else:
            # TODO 4: armar la lista "lista" con los objetos Producto elegidos
            # (usá proyecto.buscar(nombre) para cada nombre elegido),
            # crear la figura con graficar(lista, props_elegidas)
            # y mostrarla con st.pyplot(figura)
            pass

# --- Pestaña 3: resumen ---
with tab_resumen:
    if len(proyecto.productos) == 0:
        st.info("Agregá productos para ver el resumen.")
    else:
        # TODO 5: mostrar con st.dataframe(...) el resultado de
        # resumen(proyecto.productos, proyecto.nombres_propiedades())
        pass
