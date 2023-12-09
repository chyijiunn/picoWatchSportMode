## 三軸加速度感測器使用
1. 有關感測器[說明](https://patentimages.storage.googleapis.com/c7/a6/7e/e491037fced6df/CN103712632B.pdf)
2. 圖例
	- [角動量](https://www.youtube.com/watch?v=ty9QSiVC2g0)
	- [陀螺儀原理](https://kknews.cc/news/n2pzge8.html)
	- [感測器結構]
	- [MEMS Accelerometers , gyroscope](https://www.youtube.com/watch?v=KuekQ-m9xpw)
	- [走路模型](https://itw01.com/9ZHEBF9.html)
	- [幾種測試加速度模型](https://www.youtube.com/watch?v=XhBHp8tUWPQ)
		Z軸加速度為1，即為地心加速度
## 設計流程
1. 手錶顯示進入碼表模式，並可停止計時
1. 運動模式，判斷走路以及跑步數
1. 久坐提醒模式  
![](/media/io.svg)
## 程式碼
1. 練習六軸的資料，看數值變化與方向的關聯性，
1. 用上次的乒乓來試試看，若要旋轉表盤來移動，應該修改成什麼？
1. 若製作背景選單，使點可以選擇左邊或右邊的圈
1. 利用六軸的加速度方向 xyz [0]~[2] 來控制螢幕上的點
2. 利用六軸的角加速度 xyz [3]~[6] 來控制螢幕上的點
4. 做一個碼錶，利用 utime.ticks_ms() 讀取毫秒資料，中間間隔一秒後再讀第二次，兩者時間相減，顯示出毫秒差異於錶面
5. 為了有不同字型，上傳資料夾 lib 內，包含 gc9a01py 和 fonts 字型資料夾，gc9a01py顯示完文字即可顯示，不需要再 LCD.show()，但缺點是若要畫圓的 pixel 會一個點一個點畫完就 show ，時間比較慢，為了百分秒錶呈現方便性，引用 gc9a01py 較為便捷。此為gc9a01py使用範例。
1. 碼錶位數說明範例
	1. 讀取 utime.ticks_ms() 存為 N1
	2. 設定前景色與背景色
	3. while 迴圈中
		1. 讀取 utime.ticks_ms() 減去 N1 存為 N2
			- 百分秒，捨棄千分位，使用 // 10 得到商，轉為整數
			- 秒，取個位，使用 // 1000 得到商，轉為整數
			- 分，根據累積的秒 // 60 得到商，轉整數
			- 時 ，根據累積的分 // 60 得到商，轉整數
		2. 將上述資料轉字串外、分鐘顯示石為餘數資料，以 % 計算，秒數亦同，分秒取 %100 的餘數，並顯示於 LCD.text(字型,字串內容,起始x , 起始y,前景色,背景色)
7. 一個簡易碼錶範例
	- 往右傾斜進入右方後開始記錄 N1
	- 往左傾斜進入左方後記錄 N2，兩個相減得秒數差
1. 製作一個python程式間的連結，使得螢幕中的點可以移到右邊後，進入碼表程式
	1. 根據xyz[0]和 xyz[1] 可以讀取表面傾斜度
	2. 改變 pixel 出現位置，並新座標存為原本的座標
	3. 設定座標，若超過某個範圍，則引入碼表程式
		1. 碼表程式寫成一個函式，並設立 break 條件，若滿足 break 條件則跳出 while 迴圈
		2. 原始 if 條件式也需要 break，否則會再度進入碼表程式
8. 修改檔名碼錶，去掉前面數字，上傳於 pico 內，並作 import 
1. 把資料呈現出來，看看哪個軸的資料值得[記錄](https://docs.google.com/spreadsheets/d/19RdWxvHaYl9hbu7OO5hfmYfEGUUZPEqCJFpyfEXSq3c/edit?usp=sharing)
9. 讀取走路的角加速度差異值，並記錄下，需要記錄
	1.  utime.ticks_ms() 時間差
	2. 同時呈現碼錶面資料
	3. 角加速度差異
		- 利用手部晃動時，若加速度發生正負變換，就記錄
		- 同樣的方式，可以記錄跑步和走路的差異，並設立閾值(之後)

2. 寫一個計步器
3. 將運動資料轉為圖形化介面，借用上次的紅點秒針，改為繞行，但不刷新螢幕，可以填滿外圈
4. 若達成本日走路步數目標，可繞行螢幕一圈，但超過一圈顏色有所重疊，藉資料讓顏色有點變化
5. 增加跑步資料，列為內圈
1. 在裡面畫圖，使用點陣圖檔，避免記憶體會不夠用，建議[縮小解析度](https://imageresizer.com)
	- 用python3
	- 於終端機輸入 python3 18_imgtobitmap.py media/batman.bmp 4
	- 執行 18_imgtobitmap.py 這個程式 用於檔案 media/資料夾下的 batman.bmp 檔案深度為 4 位元（16色）
	- 執行後，另存檔案，含附檔名 .py，上傳到 pico 根目錄
1. LCD.bitmap(檔名.py,起始 x ,起始 y)用法
1. 錶面和時間結合在一起
1. 結合走路資料在外圈
1. 加上跑步資料在內圈
1. 為了修改環的位置，寫成函式，並加入電池資料，其中電量為遞減資料：  
	- 先畫一個環，不能放在 while 迴圈
	- 改為遞減，畫背景以抹除原本的環
1. 搭配前面蝙蝠俠，改了顏色
