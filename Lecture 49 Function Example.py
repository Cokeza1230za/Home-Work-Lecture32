def SayHello():
    print("หวัดดีไอน้อง")
    print("หวัดจั๊ฟ")
    SayHelloCoke()

def SayHelloCoke():
    print("หวัดดีไอพี่")
    print("หวัดดีไอสอง")
    SayHello()


SayHello()
SayHelloCoke()
