from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TodolistSerializer
from .models import Todolist

#GET DATA 
@api_view(['GET'])
def all_todolist(request):
    alltodolist = Todolist.objects.all() #ดึงข้อมูลจาก model Todolist
    serializer = TodolistSerializer(alltodolist,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



#POST DATA (SAVE DATABASE)
@api_view(['POST'])
def post_todolist(request):
    if request.method == 'POST':
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)



@api_view(['PUT'])
def update_todolist(request,TID):
    # localhost:8000/api/update-todolist/13
    todo = Todolist.objects.get(id=TID)

    if request.method == 'PUT':
        data = {}
        serializer = TodolistSerializer(todo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status'] = 'update'
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)



@api_view(['DELETE'])
def delete_todolist(request,TID):
    todo = Todolist.objects.get(id=TID)

    if request.method == 'DELETE':
        delete = todo.delete()
        data = {}
        if delete:
            data['status'] = 'delete'
            statuscode = status.HTTP_200_OK
        else:
            data['status'] = 'failed'
            statuscode = status.HTTP_400_BAD_REQUEST
        return Response(data=data, status=statuscode)




data = [   
    {
        "title":"แล็ปท็อปคืออะไร",
        "subtitle":"คอวพิวเตอร์คิอ อุปกรณ์ใช้สำหรับคำนวณและทำงานอื่นๆ",
        "image_url":"https://raw.githubusercontent.com/chemical-saw/BasicAPI/main/computer.jpg",
        "detail":"คอมพิวเตอร์ (อังกฤษ: computer) หรือศัพท์บัญญัติราชบัณฑิตยสภาว่า คณิตกรณ์[2][3] เป็นเครื่องจักรแบบสั่งการได้ที่ออกแบบมาเพื่อดำเนินการกับลำดับตัวดำเนินการทางตรรกศาสตร์หรือคณิตศาสตร์ โดยอนุกรมนี้อาจเปลี่ยนแปลงได้เมื่อพร้อม ส่งผลให้คอมพิวเตอร์สามารถแก้ปัญหาได้มากมาย"
    },

    {
        "title":"Flutter คือ",
        "subtitle":"This is Flutter",
        "image_url":"https://raw.githubusercontent.com/chemical-saw/BasicAPI/main/mobileapp.jpg",
        "detail":"Flutter คือ Cross-Platform Framework ที่ใช้ในการพัฒนา Native Mobile Application (Android/iOS) พัฒนาโดยบริษัท Google Inc. โดยใช้ภาษา Dart ในการพัฒนา ที่มีความคล้ายกับภาษา C# และ Javaอีกหนึ่งจุดเด่นของ Flutter คือ การปรับแต่ง UI (User Interface) ที่มีความยืนหยุ่น แยกการออกแบบเพื่อเน้นไปที่ประสบการณ์ของผู้ใช้งาน UX (User Experience) โดย UI จะใกล้เคียงกับ Native และตรงตาม Design Guideline ที่ถูกต้อง และมีความสามารถในการทำ Hot Reload ที่ทำให้การแก้ไขโค้ดสามารถแสดงผลได้ทันทีในระหว่างที่รันแอปพลิเคชัน และยังรวมไปถึงมี Widget ที่พร้อมให้เลือกใช้มากมาย ทำให้พัฒนาแอปพลิเคชันได้ไวเหมาะสำหรับองค์กรที่ต้องการแอปที่สวยงามและมีประสิทธิภาพในหลักสูตรมีการสอน State Management โดยใช้ BLoC (Business Logic Component) ที่นิยมในกลุ่มนักพัฒนา Flutter ในการจัดการ Local/Global State เพื่อรองรับระบบที่มีขนาดใหญ่และซับซ้อน ดูเป็นมืออาชีพ รวมถึงการเขียนโค้ดที่ทำงานร่วมกับ Native API โดยใช้ภาษาสมัยใหม่อย่าง Kotlin และ Swift เพื่อให้ผู้เข้าอบรมสามารถรับมือกับ Requirement ที่ต้องเชื่อมต่อกับ Native Android และ iOS"
    },
    
    {
        "title":"Python คือ",
        "subtitle":"This is Python",
        "image_url":"https://raw.githubusercontent.com/chemical-saw/BasicAPI/main/coding.jpg",
        "detail":"ภาษาไพธอน (Python) เป็นภาษาการเขียนโปรแกรมระดับสูง ที่นำข้อดีของภาษาต่างๆ มารวมไว้ด้วยกัน ถูกออกแบบมาให้เรียนรู้ได้ง่าย และมีไวยากรณ์ที่ช่วยให้เขียนโค้ดสั้นกว่าภาษาอื่นๆ มีความสามารถใช้ชนิดข้อมูลแบบไดนามิก จัดการหน่วยความจำอัตโนมัติ สนับสนุนกระบวนทัศน์การเขียนโปรแกรม (Programming paradigms) ประกอบด้วย การเขียนโปรแกรมเชิงวัตถุ (OOP : Object Oriented Programming) การเขียนโปรแกรมเชิงคำสั่ง (Imperative Programming) การเขียนโปรแกรมเชิงฟังก์ชั่น (Functional)และการเขียนโปรแกรมเชิงกระบวนการ มีลักษณะเป็นภาษาสคริปต์ที่ทำงานร่วมกับภาษาอื่นได้ มีไลบรารี่มาตรฐานมากมาย และใช้อินเตอร์พรีเตอร์แปลภาษาโปรแกรมให้ทำงานบนระบบปฎิบัติการได้หลากหลาย ทั้งบน Windows, MAC, Linux และ Unix นอกจากนั้นยังเป็นโปรแกรมแบบ Oepn source ที่นำใช้ได้ฟรี เหมาะสำหรับโปรแกรมทั้งขนาดเล็กแบะขนาดใหญ่ เช่น การสร้างเกม เฟรมเวิร์กพัฒนาเว็บ โปรแกรมที่ใช้กราฟิกติดต่อกับผู้ใช้งาน (GUI) งานคำนวนทางวิทยาศาสตร์และสถิติ งานพัฒนาซอฟแวร์ และซอฟแวร์ควบคุมระบบ เป็นต้น"
    }  
]

def Home(request):
    return JsonResponse(data=data,safe=False,json_dumps_params={'ensure_ascii': False})
