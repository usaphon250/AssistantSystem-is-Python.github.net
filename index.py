home = 'ホームサイズ'
UserName = input('あなたの名前は？：')
command_hello = input('ご用件は何でしょうか：')
command_hello_back = str(command_hello)
tenki = '晴れ'

if command_hello_back == 'おはよう':
    print('おはようございます、'+ UserName + 'さん')
elif command_hello_back == '今日の天気は？' :
    print('今日の天気は、' + tenki + 'です。')
elif command_hello_back == '天気':
    print('今日の天気は、' + tenki + 'です。')
elif command_hello_back == 'てんき':
    print('今日の天気は、' + tenki + 'です。')
elif command_hello_back == 'てんきおしえて':
    print('今日の天気は、' + tenki + 'です。')
elif command_hello_back == '今日の天気を教えて':
    print('今日の天気は、' + tenki + 'です。')
elif command_hello_back == '天気を教えて':
    print('今日の天気は、' + tenki + 'です。')
else:
    print('ワードが当てはまりませんでした')
