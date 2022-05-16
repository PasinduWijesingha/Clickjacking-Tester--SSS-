import os
import sys
import webbrowser

if len(sys.argv) != 2:
	print('\n ---------------------------- [Clickjacking Tester] ---------------------------')
	print('''             ,--,                                                                                                             
           ,---.'|                             ,--.         ,---._                                   ,--.                      
  ,----..  |   | :      ,---,  ,----..     ,--/  /|       .-- -.' \    ,---,         ,----..     ,--/  /|    ,---,.,-.----.    
 /   /   \ :   : |   ,`--.' | /   /   \ ,---,': / '       |    |   :  '  .' \       /   /   \ ,---,': / '  ,'  .' |\    /  \   
|   :     :|   ' :   |   :  :|   :     ::   : '/ /        :    ;   | /  ;    '.    |   :     ::   : '/ / ,---.'   |;   :    \  
.   |  ;. /;   ; '   :   |  '.   |  ;. /|   '   ,         :        |:  :       \   .   |  ;. /|   '   ,  |   |   .'|   | .\ :  
.   ; /--` '   | |__ |   :  |.   ; /--` '   |  /          |    :   ::  |   /\   \  .   ; /--` '   |  /   :   :  |-,.   : |: |  
;   | ;    |   | :.'|'   '  ;;   | ;    |   ;  ;          :         |  :  ' ;.   : ;   | ;    |   ;  ;   :   |  ;/||   |  \ :  
|   : |    '   :    ;|   |  ||   : |    :   '   \         |    ;   ||  |  ;/  \   \|   : |    :   '   \  |   :   .'|   : .  /  
.   | '___ |   |  ./ '   :  ;.   | '___ |   |    '    ___ l         '  :  | \  \ ,'.   | '___ |   |    ' |   |  |-,;   | |  \  
'   ; : .'|;   : ;   |   |  ''   ; : .'|'   : |.  \ /    /\    J   :|  |  '  '--'  '   ; : .'|'   : |.  \'   :  ;/||   | ;\  \ 
'   | '/  :|   ,/    '   :  |'   | '/  :|   | '_\.'/  ../  `..-    ,|  :  :        '   | '/  :|   | '_\.'|   |    \:   ' | \.' 
|   :    / '---'     ;   |.' |   :    / '   : |    \    \         ; |  | ,'        |   :    / '   : |    |   :   .':   : :-'   
 \   \ .'            '---'    \   \ .'  ;   |,'     \    \      ,'  `--''           \   \ .'  ;   |,'    |   | ,'  |   |.'     
  `---`                        `---`    '---'        "---....--'                     `---`    '---'      `----'    `---'       
                                                                                                                               
''')
	print('\n[+] Description: This tool can verify if web page is vulnerable to clickjacking !!!')
	print('\n[+] Usage: python3 clickjack.py <url>\n')
	print('\n ----------------- Created by Pasindu Wijesinghe (IT20023614) -----------------')
	print('\n')
	exit(0)

url = sys.argv[1]

html = '''
<html>
	<head>
		<title>Clickjacking Test IT20023614</title>
		<style>
		body {
 		 background-color: #301934;
        align-items: center;
		}

		h1 {
		font-size: 50px;
		font-weight: 600;
		color: #fdfdfe;
		text-shadow: 0px 0px 5px #b393d3, 0px 0px 10px #b393d3, 0px 0px 10px #b393d3,
			0px 0px 20px #b393d3;
        text-align: center;
		}
        h2 {
        font-size: 40px;
		font-weight: 600;
        color: #b393d3;
        }
        h3 {
            color: antiquewhite;
            font-size: 22pt;
        }
		</style>
	</head>

	<body>
		<h1>CLICKJACKING TEST RESULTS</h1>
        <h2 style="text-align: center;">IT20023614</h2>
        <h3 style="text-align: center;">WIJESINGHE W.M.P.M</h3>
        <hr>
		<h3>Target: <a href="%s">%s</a></h3>
		<h3>If you see the target website rendered below, it is <font color="red">VULNERABLE !!!</font>.</h3>
		<h3>If you can not see the target website rendered below, it is <font color="green">NOT VULNERABLE</font>.</h3>
        <hr> <br>
        <center>
		<iframe width="1400" height="600" src="%s"></iframe>
        </center>
		<iframe style="position: absolute; left: 200px; top: 600px; opacity: 0.8; background: AliceBlue; font-weight: bold;" src="cj-attacker.html"></iframe>
	</body>
</html>
''' % (url, url, url)

html2 = '''
<html>
	<div style="opacity: 1.0; left: 10px; top: 50px; background: PapayaWhip; font-weight: bold;">
		<center><a href="#">THIS IS AN EXAMPLE CLICKJACKING IFRAME AND LINK</a>
		<br>(Normally invisible)</center>
	</div>
</html>
'''

cjt = os.path.abspath('cj-target.html')
cja = os.path.abspath('cj-attacker.html')
localurl = 'file://' + cjt

with open(cjt, 'w') as t, open (cja, 'w') as a:
	t.write(html)
	a.write(html2) 

webbrowser.open(localurl)
print('\n ---------------------------- [Clickjacking Tester] ---------------------------')
print('''             ,--,                                                                                                             
           ,---.'|                             ,--.         ,---._                                   ,--.                      
  ,----..  |   | :      ,---,  ,----..     ,--/  /|       .-- -.' \    ,---,         ,----..     ,--/  /|    ,---,.,-.----.    
 /   /   \ :   : |   ,`--.' | /   /   \ ,---,': / '       |    |   :  '  .' \       /   /   \ ,---,': / '  ,'  .' |\    /  \   
|   :     :|   ' :   |   :  :|   :     ::   : '/ /        :    ;   | /  ;    '.    |   :     ::   : '/ / ,---.'   |;   :    \  
.   |  ;. /;   ; '   :   |  '.   |  ;. /|   '   ,         :        |:  :       \   .   |  ;. /|   '   ,  |   |   .'|   | .\ :  
.   ; /--` '   | |__ |   :  |.   ; /--` '   |  /          |    :   ::  |   /\   \  .   ; /--` '   |  /   :   :  |-,.   : |: |  
;   | ;    |   | :.'|'   '  ;;   | ;    |   ;  ;          :         |  :  ' ;.   : ;   | ;    |   ;  ;   :   |  ;/||   |  \ :  
|   : |    '   :    ;|   |  ||   : |    :   '   \         |    ;   ||  |  ;/  \   \|   : |    :   '   \  |   :   .'|   : .  /  
.   | '___ |   |  ./ '   :  ;.   | '___ |   |    '    ___ l         '  :  | \  \ ,'.   | '___ |   |    ' |   |  |-,;   | |  \  
'   ; : .'|;   : ;   |   |  ''   ; : .'|'   : |.  \ /    /\    J   :|  |  '  '--'  '   ; : .'|'   : |.  \'   :  ;/||   | ;\  \ 
'   | '/  :|   ,/    '   :  |'   | '/  :|   | '_\.'/  ../  `..-    ,|  :  :        '   | '/  :|   | '_\.'|   |    \:   ' | \.' 
|   :    / '---'     ;   |.' |   :    / '   : |    \    \         ; |  | ,'        |   :    / '   : |    |   :   .':   : :-'   
 \   \ .'            '---'    \   \ .'  ;   |,'     \    \      ,'  `--''           \   \ .'  ;   |,'    |   | ,'  |   |.'     
  `---`                        `---`    '---'        "---....--'                     `---`    '---'      `----'    `---'       
                                                                                                                               
''')
print('\n[+] Test Complete!')
print('\n[+] Thanks for using Clickjacking Tester ;-) ')
print('\n ----------------- Created by Pasindu Wijesinghe (IT20023614) -----------------')
print('\n')