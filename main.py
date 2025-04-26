import csv

# CONSTANTES
FILE_NAME = "data.csv"
DELIMITER = ","
VALID_TYPES = ["Crédito", "Débito"]

# Validar la existencia y tipo de los campos
def is_valid_row(row):
    try:
        id = int(row["id"]) >= 0
        type = True if row["tipo"] in VALID_TYPES else False
        amount = float(row["monto"]) >= 0
        return id and type and amount
    except:
        return False

if __name__ == "__main__":
    # Definición de variables
    final_balance = 0
    major_transaction = {"id": -1, "monto": -1}
    transactions_count = {"Crédito": 0, "Débito": 0}

    # Abrir el archivo CSV
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=DELIMITER)

        # Leer archivo
        for row in reader:
            if not is_valid_row(row): continue
                
            # Cálculo del balance final y conteo de transacciones
            row_ammount = float(row["monto"])
            if row["tipo"] == "Crédito":
                final_balance += row_ammount
                transactions_count["Crédito"] += 1
            else:
                final_balance -= row_ammount
                transactions_count["Débito"] += 1

            # Cálculo de la transacción mayor
            if row_ammount > major_transaction["monto"]: 
                major_transaction = {"id": int(row["id"]), "monto": row_ammount}

    # Imprimir resultados
    print(f"Reporte de Transacciones")
    print(f"--------------------------------------------------")
    print(f"Balance final: {final_balance}")
    print(f"Transacción de Mayor Monto: ID {major_transaction['id']} - {major_transaction['monto']}")
    print(f"Conteo de Transacciones: Crédito: {transactions_count['Crédito']} Débito: {transactions_count['Débito']}")