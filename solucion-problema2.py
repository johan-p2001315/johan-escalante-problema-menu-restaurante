
# PROBLEMA 2: Promociones menú de restaurante
# Curso: Fundamentos de Programación - UNAD
# Fase 5 - Evaluación Final POA

# ----------------------
# 1. DATOS INICIALES: Matriz con al menos 6 productos
# Formato: [Nombre del Producto, Categoría, Precio Base]
# ----------------------
menu = [
    ["Hamburguesa Especial", "Plato Principal", 28000],
    ["Ensalada César", "Entrante", 18000],
    ["Bandeja Paisa", "Plato Principal", 32000],
    ["Sopa de Verduras", "Entrante", 15000],
    ["Filete de Pescado", "Plato Principal", 26000],
    ["Pastel de Chocolate", "Postre", 12000],
    ["Arroz con Pollo", "Plato Principal", 24000]
]

# Definimos las condiciones de la promoción
categoria_objetivo = "Plato Principal"
umbral_precio = 25000

# ----------------------
# 2. FUNCIÓN PARA CALCULAR PRECIO FINAL
# ----------------------
def calcular_precio_final(categoria, precio_base, cat_objetivo, umbral):
    """
    Calcula el precio final aplicando la promoción si se cumplen las condiciones:
    - Si pertenece a la categoría objetivo Y precio base > umbral: 15% de descuento
    - En caso contrario: se mantiene el precio base
    """
    if categoria == cat_objetivo and precio_base > umbral:
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento
        return round(precio_final, 2), " Descuento aplicado"
    else:
        return round(precio_base, 2), " Sin descuento"

# ----------------------
# 3. GENERAR EL INFORME
# ----------------------
print("=" * 70)
print("            INFORME DE PRECIOS CON PROMOCIÓN - RESTAURANTE")
print(f"        Promoción: 15% dto. en '{categoria_objetivo}' con precio > ${umbral_precio:,}")
print("=" * 70)
print(f"{'Producto':<25} | {'Categoría':<18} | {'Precio Base':<12} | {'Precio Final':<12} | {'Estado':<20}")
print("-" * 70)

# Recorremos la matriz para procesar cada producto
for producto in menu:
    nombre = producto[0]
    cat = producto[1]
    precio_b = producto[2]
    
    precio_f, estado = calcular_precio_final(cat, precio_b, categoria_objetivo, umbral_precio)
    
    # Mostramos los datos formateados
    print(f"{nombre:<25} | {cat:<18} | ${precio_b:,.0f}       | ${precio_f:,.0f}       | {estado:<20}")

print("=" * 70)
