#список целых чисел от 0 до 999999;
#список из 99999 случайных вещественных чисел в диапазоне [-1, 1];
#42000 разных точки комплексной плоскости, лежащие на окружности радиуса r = birth_day / birth_month (можно случайных, можно равномерно распределённых);
#отрывок из книги (любой, на свой выбор) не менее 10000 слов, разбитый в список по словам.
#import random
#Random_Variable=random.sample(range(1, 18), 4) => [8, 7, 1, 4]
#8)сортировка выбором, сортировка выбора;
#7)Гномья сортировка, гномья сортировка;
#1)шейкерная сортировка, сортировка смешением
#4)сортировка вставками, сортировка вставкой;
import random
import cmath
import numpy as np
import re
import codecs

#####***************************************************************************************#####
print('\t','******** СОРТИРОВКА ВЫБОРОМ ********','\n')
#ищем максимальный элемент в неотсортированном массиве,найденный максимум меняем местами
#с последним элементом,повторяем алгоритм
Number_list=[]
for i in range(1000):
    Number_list.append(i)
random.shuffle(Number_list)
print('Исходный список:\n',Number_list,'\n')

lenght=len(Number_list)
while lenght>0:
    MAX=Number_list[0]
    for i in range(lenght):
        if Number_list[i]<MAX:
            MAX=Number_list[i]
    Number_list.remove(MAX)
    Number_list.append(MAX)
    lenght-=1
print('Отсортированный список:\n',Number_list,'\n')

#####***************************************************************************************#####
print('\t','******** ГНОМЬЯ СОРТИРОВКА ********','\n')
#если элементы стоят в нужном порядке, тогда мы переходим на следующий элемент массива, 
#если нет, то мы их переставляем и переходим на предыдущий
#обмен может породить новую пару, стоящую в неправильном порядке

#с помощь функции uniform получим равномерное распределение
Number_list=np.random.uniform(-1,1,(1000))
print('Исходный список:\n',Number_list,'\n')
lenght=len(Number_list)
i=1
while i<lenght:
    if Number_list[i-1]<=Number_list[i]:
        i+=1
    else:
        a=Number_list[i]
        Number_list[i]=Number_list[i-1]
        Number_list[i-1]=a
        i-=1
        if i==0:
            i=1
print('Отсортированный список:\n',Number_list,'\n')

#####***************************************************************************************#####
print('\t','******** ШЕЙКЕРНАЯ СОРТИРОВКА ********','\n')
#обрабатывает массив сначала слева направо, перемещая таким образом наибольший элемент в конец массива, 
#а затем справа налево, перемещая наименьший элемент в начало массива
#если при движении по части массива перестановки не происходят, то эта часть массива уже отсортирована и,
#следовательно, её можно исключить из рассмотрения
R=12.5
# R=>(Re^2 + Im^2)^1/2; R^2=>(Re^2 + Im^2);156.25=>2*Re^2;Re<=(78.125)^1/2;Re<=8.838834765
MAX=(R**(2)/2)**(0.5)
print('Модуль комплексного числа R<=',MAX,'\n')
complex_list=[]
for i in range(1000):
    Re=np.random.uniform(-MAX,MAX)
    Im=np.random.uniform(-MAX,MAX)
    complex_list.append(complex(Re,Im))
lenght=len(complex_list)
start = 0
end = lenght - 1

while start <= end:
    # идём от начала к концу
    #в конце массива окажется элемент, имеющий наибольшее значение
    for i in range(start,end, 1):
        # меняем элементы местами 
        if abs(complex_list[i]) > abs(complex_list[i + 1]):
            a=complex_list[i]
            complex_list[i] =complex_list[i+1]
            complex_list[i+1] =a
    end -= 1 #уменьшаем размер массива
    # идём от конца к началу ,в обратную сторону с шагом -1
    # в начало отправиться элемент с наименьшим значением
    for i in range(end, start, -1):
        # меняем элементы местами
        if abs(complex_list[i - 1]) > abs(complex_list[i]):
            a=complex_list[i]
            complex_list[i] = complex_list[i-1]
            complex_list[i-1] =a
    start += 1 #уменьшаем размер массива
print('Отсортированный список:\n',complex_list,'\n')

#####***************************************************************************************#####
print('\t','******** СОРТИРОВКА ВСТАВКАМИ ********','\n')
# 0-ой элемент, до 1-го элемента будет нашей отсортированной последовательностью,
#массив состоящий из одного элемента является отсортированным
#на каждом шаге алгоритма мы берем один из элементов массива, находим позицию для вставки и вставляем
#в котором элементы входной последовательности просматриваются по одному, 
#и каждый новый поступивший элемент размещается в подходящее место среди ранее упорядоченных элементов

#реестр кодировок. открыть текстовый файл, закодированный с использованием utf-8 кодировки
file= codecs.open( "C:/1/tress.txt", "r", "utf_8_sig" )
#чтение в строку
f=file.read()
#воспользуемся sub удаления занков препинания по шаблону: r'[^\w\s]'
l= re.sub(r'[^\w\s]','', f)
# разделим строку на список по пробелам
List=l.split()

length = len(List) 
for i in range(1, len(List)):
        k = len(List[i])
        t=List[i]
        j = i-1
        # ищем место для вставки
        while j >=0 and k < len(List[j]) :
            #сдвигаем минимальный элемент назад,максимальный вперёд
            List[j+1] = List[j]
            #индекс смещаем назад для рассмотрения леволежащего элемента
            j -= 1
        #устанавливаем минимальный элемент на свое место в списке
        List[j+1] = t 
print(List)
file.close()