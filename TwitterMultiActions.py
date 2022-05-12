import requests
import json
import os
import sys
import random
import ctypes
import urllib3
from msvcrt import getch
from datetime import datetime
from colorama import Fore

urllib3.disable_warnings()

useragents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 11.4; rv:89.0) Gecko/20100101 Firefox/89.0','Mozilla/5.0 (X11; Linux i686; rv:89.0) Gecko/20100101 Firefox/89.0','Mozilla/5.0 (Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:89.0) Gecko/20100101 Firefox/89.0','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0','Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15','Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; Trident/4.0;)','Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)','Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.0)','Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2)','Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 6.2; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 Edg/91.0.864.37','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 Edg/91.0.864.37','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 OPR/77.0.4054.64','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 OPR/77.0.4054.64','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 OPR/77.0.4054.64','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 OPR/77.0.4054.64','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 Vivaldi/4.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 Vivaldi/4.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 Vivaldi/4.0','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 Vivaldi/4.0','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 Vivaldi/4.0','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 YaBrowser/21.5.0 Yowser/2.5 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 YaBrowser/21.5.0 Yowser/2.5 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 YaBrowser/21.5.0 Yowser/2.5 Safari/537.36','Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.80 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.80 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPod; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.80 Mobile/15E148 Safari/604.1','Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36','Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/34.0 Mobile/15E148 Safari/605.1.15','Mozilla/5.0 (iPad; CPU OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/34.0 Mobile/15E148 Safari/605.1.15','Mozilla/5.0 (iPod touch; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) FxiOS/34.0 Mobile/15E148 Safari/605.1.15','Mozilla/5.0 (Android 11; Mobile; rv:68.0) Gecko/68.0 Firefox/89.0','Mozilla/5.0 (Android 11; Mobile; LG-M255; rv:89.0) Gecko/89.0 Firefox/89.0','Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPod touch; CPU iPhone 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1','Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36 EdgA/46.3.4.5155','Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36 EdgA/46.3.4.5155','Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36 EdgA/46.3.4.5155','Mozilla/5.0 (Linux; Android 10; ONEPLUS A6003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36 EdgA/46.3.4.5155','Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 EdgiOS/46.3.13 Mobile/15E148 Safari/605.1.15','Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Mobile Safari/537.36 Edge/40.15254.603','Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36 OPR/63.3.3216.58675','Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36 OPR/63.3.3216.58675','Mozilla/5.0 (Linux; Android 10; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36 OPR/63.3.3216.58675','Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 YaBrowser/21.5.3.836 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 YaBrowser/21.5.3.836 Mobile/15E148 Safari/605.1','Mozilla/5.0 (iPod touch; CPU iPhone 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 YaBrowser/21.5.3.836 Mobile/15E148 Safari/605.1','Mozilla/5.0 (Linux; arm_64; Android 11; SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 YaBrowser/21.3.4.59 Mobile Safari/537.36']

os.system("cls")
ctypes.windll.kernel32.SetConsoleTitleW('TwitterMultiActions | by NAZAVOD')
print('Telegram Channel - https://t.me/n4z4v0d\nИнструкция - https://telegra.ph/TwitterMultiActions--tmen4z4v0d-11-30\n')
clear = lambda: os.system('cls')

while True:
	try:
		print('Введите число того, что хотите использовать далее\n')
		print('1. Массовая подписка\n2. Массовые ретвиты\n3. Массовые лайки\n4. Массовые комментарии WAX кошелька в комментарии')
		action = int(input())
		clear()
		if action == 1:
			print('Введите юзернейм профиля для подписки (без @)\n>> ', end='')
			usernametosubscribe = str(input())
		else:
			print('Введите ссылку на твит для репоста/лайка\n>> ', end='')
			tweetlink = str(input())
			tweetid = tweetlink.split('status/')[-1]

		print("Использовать прокси? (Y/N)\n>> ", end='')
		useproxy = input()
		if useproxy in ('y','Y'):
		    print("Введите тип прокси (https/socks4/socks5)\n>> ", end="")
		    proxytype = input()
		if 0 < action < 5:
			break
	except:
		print('\nОшибка!')

# Загрузка аккаунтов
# <--
print('')
file = open("accounts.txt", "r")
lines = file.readlines()

cookies = []

try:
	for line in lines:
		if 'cookie' in line:
			cookies.append(line.strip().split('cookie: ')[-1])
		elif line == '\n':
			pass
		else:
			print(Fore.RED + datetime.now().strftime("%H:%M:%S") + ' | Ошибка во время загрузки аккаунтов')
			break
	accountsnum = len(cookies)
except:
	print(Fore.RED + datetime.now().strftime("%H:%M:%S") + ' | Ошибка во время загрузки аккаунтов')
finally:
	file.close()
	print(Fore.GREEN + datetime.now().strftime("%H:%M:%S") + ' | Успешно загружено '+str(accountsnum)+' аккаунтов')
# -->
# Загрузка аккаунтов

# Загрузка кошельков
# <--
if action == 4:
	file = open("waxwallets.txt", "r")
	lines = file.readlines()

	waxwallets = []

	try:
		for line in lines:
			waxwallets.append(line.strip())
	except:
		print(Fore.RED + datetime.now().strftime("%H:%M:%S") + ' | Ошибка во время загрузки кошельков')
	finally:
		file.close()
		print(Fore.GREEN + datetime.now().strftime("%H:%M:%S") + ' | Успешно загружено '+str(len(waxwallets))+' кошельков')
# -->
# Загрузка кошельков

# <--
# Загрузка прокси
if useproxy in ('y','Y'):
	file = open("proxy.txt", "r")
	lines = file.readlines()

	proxies = []

	try:
		for line in lines:
			if line == '\n':
				pass
			else:
				proxies.append(line.strip())
	except:
		print(Fore.RED + datetime.now().strftime("%H:%M:%S") + ' | Ошибка во время загрузки прокси')
	finally:
		file.close()
		print(Fore.GREEN + datetime.now().strftime("%H:%M:%S") + ' | Успешно загружено '+str(len(proxies))+' прокси')
# -->
# Загрузка прокси

if useproxy in ('y', 'Y'):
	if len(cookies) != len(proxies):
		print(Fore.RED + datetime.now().strftime("%H:%M:%S") + ' | Количество прокси не равно количеству аккаунтов, ошибка')
		print('\n' + Fore.RED + datetime.now().strftime("%H:%M:%S") + ' | Нажмите любую клавишу для выхода')
		getch()
		sys.exit()

# Первичная настройка (токены хуекины)
# <--
print('')
session = requests.Session()
session.headers.update({'User-Agent': random.choice(useragents), 'Origin': 'https://mobile.twitter.com', 'Referer': 'https://mobile.twitter.com/', 'x-twitter-active-user': 'yes', 'x-twitter-auth-type': 'OAuth2Session', 'x-twitter-client-language': 'en', 'content-type': 'application/x-www-form-urlencoded'})
r = session.get('https://abs.twimg.com/responsive-web/client-web/main.f3ada2b5.js', verify=False)
queryIdforSubscribe = r.text.split('",operationName:"TweetResultByRestId",operationType:"query",metadata:{featureSwitches:[]}}},fDBV:function(e,t){e.exports={queryId:"')[-1].split('"')[0]
queryIdforRetweet = r.text.split('"/share","/terms","/tos","/transparency","/tweetbutton","/user_spam_reports"]}')[-1].split(',operationName:"CreateRetweet')[0].split('queryId:"')[-1].split('"')[0]
queryIdforLike = r.text.split('"x/WR":function(e,t){e.exports={queryId:"')[-1].split('"')[0]
queryIdforComment = r.text.split('operationName:"ListProductSubscriptions",operationType:"query"')[-1].split('operationName:"CreateTweet')[0].split('queryId:"')[-1].split('"')[0]
quertIdforFollowers = r.text.split('QK8Q:function(e,t){e.exports={queryId:"')[-1].split('"')[0]
bearertoken = 'Bearer '+r.text.split('const r="ACTION_FLUSH",i="ACTION_REFRESH')[-1].split(',l="d_prefs"')[0].split(',s="')[-1].split('"')[0]
# -->
# Первичная настройка

for i in range(accountsnum):
	if useproxy in ('y','Y'):
		proxiestr = {'http': 'http://'+proxies[i],'https': proxytype+'://'+proxies[i]}
		session.proxies.update(proxiestr)
	cookiestr = cookies[i]
	csrftoken = cookiestr.split('ct0=')[-1].split(';')[0]
	session.headers.update({'authorization': bearertoken, 'cookie': cookiestr, 'x-csrf-token': csrftoken})

	# <--
	# Получить юзернейм
	r = session.get('https://mobile.twitter.com/i/api/1.1/account/settings.json?include_mention_filter=true&include_nsfw_user_flag=true&include_nsfw_admin_flag=true&include_ranked_timeline=true&include_alt_text_compose=true&ext=ssoConnections&include_country_code=true&include_ext_dm_nsfw_media_filter=true&include_ext_sharing_audiospaces_listening_data_with_followers=true', verify=False)
	username = json.loads(r.text)['screen_name']
	# -->
	# Получить юзернейм


	# <--
	# Выполнение подписок
	if action == 1:
			# <--
			# Получить restid профиля для подписки
		r = session.get('https://mobile.twitter.com/i/api/graphql/'+queryIdforSubscribe+'/UserByScreenName?variables={"screen_name":"'+usernametosubscribe+'","withSafetyModeUserFields":true,"withSuperFollowsUserFields":true}', verify=False)
		restid = str(json.loads(r.text)['data']['user']['result']['rest_id'])
			# -->
			# Получить restid профиля для подписки
		r = session.post('https://mobile.twitter.com/i/api/1.1/friendships/create.json', data='include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_has_nft_avatar=1&skip_status=1&id='+restid, verify=False)
		try:
			json.loads(r.text)['id']
			print(Fore.GREEN + datetime.now().strftime("%H:%M:%S") + ' | Успешно подписался | '+username)
		except:
			print(Fore.RED + datetime.now().strftime("%H:%M:%S") + ' | Ошибка во время подписки | '+username)
	# -->
	# Выполнение подписок

	# <--
	# Выполнение ретвитов
	elif action == 2:
		r = session.post('https://mobile.twitter.com/i/api/graphql/'+queryIdforRetweet+'/CreateRetweet', headers={'content-type': 'application/json'}, json={"variables":"{\"tweet_id\":\""+tweetid+"\",\"dark_request\":false}","queryId":""+queryIdforRetweet+""}, verify=False)
		try:
			print(Fore.RED + datetime.now().strftime("%H:%M:%S") + " | Ошибка: "+json.loads(r.text)['errors'][0]['message']+" | "+username)
		except:
			print(Fore.GREEN + datetime.now().strftime("%H:%M:%S") + " | Успешно ретвитнул | "+username)
	# -->
	# Выполнение ретвитов

	# <--
	# Выполнение лайка
	elif action == 3:
		r = session.post('https://mobile.twitter.com/i/api/graphql/'+queryIdforLike+'/FavoriteTweet', headers={'content-type': 'application/json'}, json={"variables":"{\"tweet_id\":\""+tweetid+"\",\"dark_request\":false}","queryId":""+queryIdforRetweet+""}, verify=False)
		try:
			print(Fore.RED + datetime.now().strftime("%H:%M:%S") + " | Ошибка: "+json.loads(r.text)['errors'][0]['message']+" | "+username)
		except:
			print(Fore.GREEN + datetime.now().strftime("%H:%M:%S") + " | Успешно ретвитнул | "+username)
	# -->
	# Выполнение лайка

	# <--
	# WAX кошелек в комментарии
	elif action == 4:
		waxwallet = waxwallets[i]
		r = session.post('https://mobile.twitter.com/i/api/graphql/'+queryIdforComment+'/CreateTweet', headers={'content-type': 'application/json'}, json={"variables":"{\"tweet_text\":\""+waxwallet+"\n@"+str(randomsubscribers[0])+"\n@"+str(randomsubscribers[1])+"\n@"+str(randomsubscribers[2])+"\",\"reply\":{\"in_reply_to_tweet_id\":\""+tweetid+"\",\"exclude_reply_user_ids\":[]},\"media\":{\"media_entities\":[],\"possibly_sensitive\":false},\"withDownvotePerspective\":false,\"withReactionsMetadata\":false,\"withReactionsPerspective\":false,\"withSuperFollowsTweetFields\":true,\"withSuperFollowsUserFields\":true,\"semantic_annotation_ids\":[],\"dark_request\":false,\"withUserResults\":true,\"withBirdwatchPivots\":false}","queryId":""+queryIdforComment+""}, verify=False)
		try:
			print(Fore.RED + datetime.now().strftime("%H:%M:%S") + " | Ошибка: "+json.loads(r.text)['errors'][0]['message']+" | "+username)
		except:
			print(Fore.GREEN + datetime.now().strftime("%H:%M:%S") + " | Успешно прокоменнтировал | "+username)
			del randomsubscribers[0]
			del randomsubscribers[1]
			del randomsubscribers[2]
	# -->
	# WAX кошелек в комментарии

print('\n' + Fore.GREEN + datetime.now().strftime("%H:%M:%S") + ' | Работа успешно завершена! Нажмите любую клавишу для выхода')
getch()
sys.exit()