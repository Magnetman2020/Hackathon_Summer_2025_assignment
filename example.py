#1. Hello World
print('hello world')

#2. greet関数の実装、「こんにちは」と出力
def greet():
    print("こんにちは")

 #関数の呼び出し
greet()

#3. 私の名前は{name}
def print_name(name):
    print(f"私の名前は{name}です")

 #関数の呼び出し
print_name("daisuke")

#4. get_greet関数　戻り値「おはようございます」としてprint関数で呼び出し
def get_greet():
    return "おはようございます"

x=get_greet()
print(x)

#5. a, bを引数としたadd関数 print関数で出力
def add(a, b):
    return a + b

result = add(1, 2)
print(result)

#6. example.htmlを作成して「hello world」と画面に表示