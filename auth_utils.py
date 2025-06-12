import csv

def simpan_ke_csv_user(username, password, role, filename="training_user.csv"):
    headers = ["USERNAME", "PASSWORD", "ROLE"]
    user_data = {"USERNAME": username, "PASSWORD": password, "ROLE": role}
    
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(user_data)

def baca_dari_csv_user(filename="training_user.csv"):
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file CSV: {e}")
        return []

def sign_up():
    username = input("Masukkan username: ")
    users = baca_dari_csv_user()
    if any(user["USERNAME"] == username for user in users):
        print("Username sudah digunakan. Silakan coba lagi.")
        return None
    
    password = input("Masukkan password: ")
    print("Pilih role:")
    print("1. Pengusaha")
    print("2. Investor")
    role_choice = input("Masukkan pilihan (1/2): ")
    role = "Pengusaha" if role_choice == "1" else "Investor" if role_choice == "2" else None
    
    if not role:
        print("Pilihan role tidak valid.")
        return None
    
    simpan_ke_csv_user(username, password, role)
    print("Sign up berhasil!")
    return {"username": username, "role": role}

def log_in():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    users = baca_dari_csv_user()
    
    for user in users:
        if user["USERNAME"] == username and user["PASSWORD"] == password:
            print("Log in berhasil!")
            return {"username": username, "role": user["ROLE"]}
    
    print("Username atau password salah.")
    return None