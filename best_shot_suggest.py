import tkinter
from PIL import Image, ImageTk, ImageFont, ImageDraw
import cv2
import numpy as np


###ベストショットの番号を配列で受け取る###
import best_shot
#best_shotのnumberという関数でベストショットの番号を返す
best_shot_number = best_shot.number()
print(best_shot_number)
####################################


#表示画像のインデックス
big_image_index = 0
thumbnail_image_index = 0

#サムネイル
t_btn1 = None
t_btn2 = None
t_btn3 = None
t_btn4 = None
t_btn5 = None
t_btn6 = None
t_btn7 = None
t_btn8 = None
t_btn9 = None
t_btn10 = None
t_btn11 = None
t_btn12 = None
t_btn13 = None
t_btn14 = None
t_btn15 = None 


# --- 基本的な表示準備 ----------------                                         
window = tkinter.Tk()
window.geometry("1920x1080") # 画面サイズ                   
window.title("ベストショットサジェストβ")

###画像サイズ設定###
big_image_width = 700
big_image_height = 400

thumbnail_image_width = 70
thumbnail_image_height = 40

###切り取り画像一括読み取り###
flame_data = []
thumbnail_data = []

for num in range(0,500,1):
    img = Image.open('flame_data/sample_video_img_' + str(num).rjust(4, '0') + '.png')
    
    #選択画像作成
    b_img = img.resize((big_image_width, big_image_height))
    b_img = ImageTk.PhotoImage(b_img)
    flame_data.append(b_img)
    
    #サムネイル画像作成
    t_img = img.resize((thumbnail_image_width, thumbnail_image_height))
    t_img = ImageTk.PhotoImage(t_img)
    thumbnail_data.append(t_img)
    
#########################

# 画像を指定                                                                   

# canvasサイズも画面サイズと同じにして描画    
canvas = tkinter.Canvas(width=1920, height=1080)
canvas.place(x=0, y=0)
# -------------------------------------                                         
# キャンバスに画像を表示する                                                    
canvas.create_image(big_image_width/4, big_image_height/4, image=flame_data[big_image_index], anchor=tkinter.NW,tag='big_image')

###画像に文字を入れる関数###
def img_add_msg(img, message):
    font_path = '/System/Library/Fonts/ヒラギノ角ゴシック W9.ttc'# Windowsのフォントファイルへのパス
    font_size = 40                                      # フォントサイズ
    font = ImageFont.truetype(font_path, font_size)     # PILでフォントを定義
    img = Image.fromarray(img)                          # cv2(NumPy)型の画像をPIL型に変換
    draw = ImageDraw.Draw(img)                          # 描画用のDraw関数を用意

    # テキストを描画（位置、文章、フォント、文字色（BGR+α）を指定）
    draw.text((150, 600), message, font=font, fill=(0, 0, 255, 0))
    img = np.array(img)                                 # PIL型の画像をcv2(NumPy)型に変換
    return img                                          # 文字入りの画像をリターン

######################


###画像生成###
def generate_image():
    #TODO:絵コンテ書き出し
    img = cv2.imread('flame_data/sample_video_img_' + str(big_image_index).rjust(4, '0') + '.png', 1)                         # カラー画像読み込み
    message = 'これは要約文です。これは要約文です。これは要約文です。これは要約文です。'# 画像に入れる文章
    img = img_add_msg(img, message)                         # 画像に文字を入れる関数を実行
    cv2.imwrite('sample4.png', img)                         #画像を保存する
    print("画像書き出し成功")

#############

#生成ボタン作成
btn = tkinter.Button(window, text="生成", font=("MSゴシック", "30", "bold"),command=generate_image)
#生成ボタン表示
btn.place(x=1000, y=230, width=150, height=40)

label = tkinter.Label(window, text="画像選択ツールβ",font=("MSゴシック","50"), bg="#faaaff")
label.pack()

###画面遷移イベント###
def right_btn_click():
    global big_image_index
    canvas.delete('big_image')
    big_image_index += 1
    canvas.create_image(big_image_width/4, big_image_height/4, image=flame_data[big_image_index], anchor=tkinter.NW,tag='big_image')
    
def left_btn_click():
    global big_image_index
    if(big_image_index > 0):
        canvas.delete('big_image')
        big_image_index -= 1
        canvas.create_image(big_image_width/4, big_image_height/4, image=flame_data[big_image_index], anchor=tkinter.NW,tag='big_image')
    
def thumbnail_click(image_index):
    global big_image_index
    canvas.delete('big_image')
    big_image_index = image_index
    canvas.create_image(big_image_width/4, big_image_height/4, image=flame_data[big_image_index], anchor=tkinter.NW,tag='big_image')
####################

###サムネイル一覧イベント###
def thumbnail():
    global thumbnail_image_index
    global t_btn1
    global t_btn2
    global t_btn3
    global t_btn4
    global t_btn5
    global t_btn6
    global t_btn7
    global t_btn8
    global t_btn9
    global t_btn10
    global t_btn11
    global t_btn12
    global t_btn13
    global t_btn14
    global t_btn15
    
    #サムネイル削除
    if(t_btn1):
        t_btn1.destroy()
        t_btn2.destroy()
        t_btn3.destroy()
        t_btn4.destroy()
        t_btn5.destroy()
        t_btn6.destroy()
        t_btn7.destroy()
        t_btn8.destroy()
        t_btn9.destroy()
        t_btn10.destroy()
        t_btn11.destroy()
        t_btn12.destroy()
        t_btn13.destroy()
        t_btn14.destroy()
        t_btn15.destroy()
    
    #サムネイル生成
    if(thumbnail_image_index in best_shot_number):
        t_btn1=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index],highlightbackground='red',command=lambda:thumbnail_click(thumbnail_image_index))
    else:
        t_btn1=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index],command=lambda:thumbnail_click(thumbnail_image_index))
    t_btn1.pack(ipadx=0,ipady=0,side = 'left',anchor='sw')
    
    if(thumbnail_image_index+1 in best_shot_number):
        t_btn2=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+1],highlightbackground='red',command=lambda:thumbnail_click(thumbnail_image_index+1))
    else:
        t_btn2=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+1],command=lambda:thumbnail_click(thumbnail_image_index+1))
    t_btn2.pack(ipadx=0,ipady=0,side = 'left',anchor='sw')
    
    if(thumbnail_image_index+2 in best_shot_number):
        t_btn3=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+2],highlightbackground='red',command=lambda:thumbnail_click(thumbnail_image_index+2))
    else:
        t_btn3=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+2],command=lambda:thumbnail_click(thumbnail_image_index+2))
    t_btn3.pack(ipadx=0,ipady=0,side = 'left',anchor='sw')
    
    if(thumbnail_image_index+3 in best_shot_number):
        t_btn4=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+3],highlightbackground='red',command=lambda:thumbnail_click(thumbnail_image_index+3))
    else:
        t_btn4=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+3],command=lambda:thumbnail_click(thumbnail_image_index+3))
    t_btn4.pack(ipadx=0,ipady=0,side = 'left',anchor='sw')
    
    if(thumbnail_image_index+4 in best_shot_number):
        t_btn5=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+4],highlightbackground='red',command=lambda:thumbnail_click(thumbnail_image_index+4))
    else:
        t_btn5=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+4],command=lambda:thumbnail_click(thumbnail_image_index+4))
    t_btn5.pack(ipadx=0,ipady=0,side = 'left',anchor='sw')
    
    if(thumbnail_image_index+5 in best_shot_number):
        t_btn6=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+5],highlightbackground='red',command=lambda:thumbnail_click(thumbnail_image_index+5))
    else:
        t_btn6=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+5],command=lambda:thumbnail_click(thumbnail_image_index+5))
    t_btn6.pack(ipadx=0,ipady=0,side = 'left',anchor='sw')
    
    if(thumbnail_image_index+6 in best_shot_number):
        t_btn7=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+6],highlightbackground='red',command=lambda:thumbnail_click(thumbnail_image_index+6))
    else:
        t_btn7=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+6],command=lambda:thumbnail_click(thumbnail_image_index+6))
    t_btn7.pack(ipadx=0,ipady=0,side = 'left',anchor='sw')
    
    if(thumbnail_image_index+7 in best_shot_number):
        t_btn8=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+7],highlightbackground='red',command=lambda:thumbnail_click(thumbnail_image_index+7))
    else:
        t_btn8=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+7],command=lambda:thumbnail_click(thumbnail_image_index+7))
    t_btn8.pack(ipadx=0,ipady=0,side = 'left',anchor='sw')
    
    if(thumbnail_image_index+8 in best_shot_number):
        t_btn9=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+8],highlightbackground='red',command=lambda:thumbnail_click(thumbnail_image_index+8))
    else:
        t_btn9=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+8],command=lambda:thumbnail_click(thumbnail_image_index+8))
    t_btn9.pack(ipadx=0,ipady=0,side = 'left',anchor='sw')
    
    if(thumbnail_image_index+9 in best_shot_number):
        t_btn10=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+9],highlightbackground='red',command=lambda:thumbnail_click(thumbnail_image_index+9))
    else:
        t_btn10=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+9],command=lambda:thumbnail_click(thumbnail_image_index+9))
    t_btn10.pack(ipadx=0,ipady=0,side = 'left',anchor='sw')
    
    if(thumbnail_image_index+10 in best_shot_number):
        t_btn11=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+10],highlightbackground='red',command=lambda:thumbnail_click(thumbnail_image_index+10))
    else:
        t_btn11=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+10],command=lambda:thumbnail_click(thumbnail_image_index+10))
    t_btn11.pack(ipadx=0,ipady=0,side = 'left',anchor='sw')
    
    if(thumbnail_image_index+11 in best_shot_number):
        t_btn12=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+11],highlightbackground='red',command=lambda:thumbnail_click(thumbnail_image_index+11))
    else:
        t_btn12=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+11],command=lambda:thumbnail_click(thumbnail_image_index+11))
    t_btn12.pack(ipadx=0,ipady=0,side = 'left',anchor='sw')
    
    if(thumbnail_image_index+12 in best_shot_number):
        t_btn13=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+12],highlightbackground='red',command=lambda:thumbnail_click(thumbnail_image_index+12))
    else:
        t_btn13=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+12],command=lambda:thumbnail_click(thumbnail_image_index+12))
    t_btn13.pack(ipadx=0,ipady=0,side = 'left',anchor='sw')
    
    if(thumbnail_image_index+13 in best_shot_number):
        t_btn14=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+13],highlightbackground='red',command=lambda:thumbnail_click(thumbnail_image_index+13))
    else:
        t_btn14=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+13],command=lambda:thumbnail_click(thumbnail_image_index+13))
    t_btn14.pack(ipadx=0,ipady=0,side = 'left',anchor='sw')
    
    if(thumbnail_image_index+14 in best_shot_number):
        t_btn15=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+14],highlightbackground='red',command=lambda:thumbnail_click(thumbnail_image_index+14))
    else:
        t_btn15=tkinter.Button(text='bottom',image=thumbnail_data[thumbnail_image_index+14],command=lambda:thumbnail_click(thumbnail_image_index+14))
    t_btn15.pack(ipadx=0,ipady=0,side = 'left',anchor='sw')

#サムネイル+15一覧
def plus_thumbnail_15():
    global thumbnail_image_index
    thumbnail_image_index += 15
    thumbnail()
    #TODO:最大値を超えないように設定

#サムネイル-15一覧
def minus_thumbnail_15():
    global thumbnail_image_index
    if(thumbnail_image_index > 0):
        thumbnail_image_index -= 15
        thumbnail()
    else:
        print("indexが0以下です")

#####################

# 遷移ボタン「左」
right_btn=tkinter.Button(text='←',command=left_btn_click)
right_btn.pack(ipadx=20,ipady=5,side = 'top',anchor='nw')

# 遷移ボタン「右」
right_btn=tkinter.Button(text='→',command=right_btn_click)
right_btn.pack(ipadx=20,ipady=5,side = 'top',anchor='nw')

# サムネイル遷移ボタン「+15」
right_btn=tkinter.Button(text='+15',command=plus_thumbnail_15)
right_btn.pack(ipadx=20,ipady=5,side = 'top',anchor='nw')

# サムネイル遷移ボタン「-15」
right_btn=tkinter.Button(text='-15',command=minus_thumbnail_15)
right_btn.pack(ipadx=20,ipady=5,side = 'top',anchor='nw')

# サムネイル生成
thumbnail()

window.mainloop()