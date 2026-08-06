import time

def verify_student():
    print("verify_student")
    time.sleep(2)
    print("strudent verified\n")

def fetch_attendance():
    print("fetching attendanc")
    time.sleep(3)
    print("attendance loaded\n")    

def fetch_marks():
    print("fetching marks")
    time.sleep(2)
    print("attendance loaded\n")
    print("====student portal====\n")


start = time.time()
verify_student()
fetch_attendance()
fetch_marks()

end=time.time()
print(f"\nTotal time={end-start:.2f} second")