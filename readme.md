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
![](/media/watch.svg)
## 程式碼
1. 練習六軸的資料，看數值變化與方向的關聯性，利用六軸的加速度方向 xyz [0]~[2] 來控制螢幕上的點
2. 利用六軸的角加速度 xyz [3]~[6] 來控制螢幕上的點
3. 若製作背景選單，使點可以選擇左邊或右邊的圈
4. 做一個碼表，利用 utime.ticks_ms() 讀取毫秒資料，中間間隔一秒後再讀第二次，兩者時間相減，顯示出毫秒差異於錶面
5. 為了有不同字型，上傳資料夾 lib 內，包含 gc9a01py 和 fonts 字型資料夾，gc9a01py顯示完文字即可顯示，不需要再 LCD.show()，但缺點是若要畫圓的 pixel 會一個點一個點畫完就 show ，時間比較慢，為了百分秒錶呈現方便性，引用 gc9a01py 較為便捷。
	1. 讀取 utime.ticks_ms() 存為 N1
	2. 設定前景色與背景色
	3. while 迴圈中
		1. 讀取 utime.ticks_ms() 減去 N1 存為 N2
			- 百分秒，捨棄千分位，使用 // 10 得到商，轉為整數
			- 秒，取個位，使用 // 1000 得到商，轉為整數
			- 分，根據累積的秒 // 60 得到商，轉整數
			- 時 ，根據累積的分 // 60 得到商，轉整數
		2. 將上述資料轉字串外、分鐘顯示石為餘數資料，以 % 計算，秒數亦同，分秒取 %100 的餘數，並顯示於 LCD.text(字型,字串內容,起始x , 起始y,前景色,背景色)
6. 一個短暫的碼表範例
7. 製作一個選單，使得螢幕中的點可以移到右邊後，進入碼表程式
	1. 根據xyz[0]和 xyz[1] 可以讀取表面傾斜度
	2. 改變 pixel 出現位置，並新座標存為原本的座標
	3. 設定座標，若超過某個範圍，則引入碼表程式
		1. 碼表程式寫成一個函式，並設立 break 條件，若滿足 break 條件則跳出 while 迴圈
		2. 原始 if 條件式也需要 break，否則會再度進入碼表程式
8. 修改後的碼錶
9. 讀取走路的角加速度差異值，並記錄下，需要記錄
	1.  utime.ticks_ms() 時間差
	2. 同時呈現碼錶面資料
	3. 角加速度差異
		- 利用手部晃動時，若加速度發生正負變換，就記錄
		- 同樣的方式，可以記錄跑步和走路的差異，並設立閾值(之後)
1. 把走路資料寫出來，看看哪個軸的資料值得[記錄](https://docs.google.com/spreadsheets/d/19RdWxvHaYl9hbu7OO5hfmYfEGUUZPEqCJFpyfEXSq3c/edit?usp=sharing)
2. 寫一個計步器
3. 將運動資料轉為圖形化介面，借用上次的紅點秒針，改為繞行，但不刷新螢幕，可以填滿外圈
4. 若達成本日走路步數目標，可繞行螢幕一圈
5. 增加跑步資料，列為內圈