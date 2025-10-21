from app.config.database import get_connection

def save_to_db(data: dict):
    """Salva os dados no banco de dados MySQL, usando apenas 'variavel' e 'valor'."""
    conn = get_connection()
    
    
    db_variavel = data.get('variable', 'N/A')
    db_valor = data.get('value', 'N/A')
    
    if db_variavel == 'N/A' or db_valor == 'N/A':
        print(f"AVISO: Payload incompleto. Variável ou Valor ausentes. Chaves recebidas: {list(data.keys())}")
        conn.close()
        return

    cursor = conn.cursor()
    
    sql = """
        INSERT INTO data (variavel, valor)
        VALUES (%s, %s)
    """
    
    values = (
        db_variavel, 
        db_valor,    
    )
    
    try:
        cursor.execute(sql, values)
        conn.commit()
        print(f"Dados salvos com sucesso. Variável: {db_variavel}, Valor: {db_valor}")
    except Exception as e:
        print(f"Erro ao inserir no DB: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def list_data(limt: int = 50):
    """Lista todos os dados armazenados no banco de dados MySQL"""
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    # AJUSTE A COLUNA DA CLÁUSULA ORDER BY
    cursor.execute("SELECT * FROM data ORDER BY id DESC LIMIT %s", (limt,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def get_by_device(device_id: str):
    """
    Busca registros por dispositivo específico
    ⚠️ ATENÇÃO: Esta função NÃO funcionará mais, pois a coluna 'dispositivo' foi removida.
    Você deve removê-la da rota ou refazê-la para buscar por 'variavel'.
    """
    return []