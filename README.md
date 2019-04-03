# HUGIN-MUNIN-player-plugin
<img src="https://i.imgur.com/8aBMIR8.png" width = "200" height = "200"/>
　　此專題以胡金與穆寧為名。祂們是北歐神話中在眾神之王奧丁（執行演算的程式）雙耳邊報告所見所聞的兩隻烏鴉，分別代表著思緒（使用者喜好）與記憶（運算根據的數值紀錄）。
主要目標是希望在樹莓派上運行的 Volumio 播放系統所控制的 MPD(Music Player Daemon)內，加入使用 LADSPA (Linux Audio Developers Simple Plugin API)撰寫的強化版的 40 段等化器插件，並提供使用者一條初始的等化曲線。
根據每次使用者主觀選擇喜不喜歡當前的等化曲線所播放出的音響效果後，利用基因演算法運算並調整等化器的曲線數值，最後使音樂透過 ALSA(Advanced Linux Sound Architecture)從 HiFiBerry DAC+音效卡上播出，讓所呈現的音響效果能漸趨適應使用者的偏好。

---
### 系統架構與流程
<img src="https://i.imgur.com/OiarcHb.jpg" width = "560" height = "320"/><img src="https://i.imgur.com/maHeEEL.jpg" width = "100" height = "300"/>
---

### rPi3環境準備
音效卡：HiFiBerry DAC+\
系統：[已安裝好可自行撰寫LADSPA plugin的Volumio映像檔](https://drive.google.com/open?id=1zqb10P6CvRy5yy96RGitqSoSBvn1M0gR)\
（安裝步驟繁瑣，需要FFTW library等，也會因版本而異，有機會再另外寫一篇詳細說明安裝方式）
* *index.html    (ui)*\
取代/volumio/http/www/index.html，並將IP改為rPi的IP。
* *Hugin.js    (shell)*\
置於rPi上並將IP改為server的IP。\
在樹莓派上運作的程式，利用ssh 連接並執行。負責接收使用者的喜好選擇並與歌曲資訊一起傳輸給穆寧，以及接收其回傳的數值去下指令更改等化器。
* *Munun.js    (server)*\
在伺服器主機端上運行的程式。負責接收使用者資訊並執行程式奧丁，使其根據資料運算出新的曲線後，再將數值回傳給胡金。歷次的選擇與數值皆會被記錄。
* *Odin.py    (GA algorithm)*\
與Munin置於相同路徑下。
* *Hvergelmir.js    (refresh)*\
置於rPi中。
---
### 新增[40_band_eq](https://hackmd.io/s/rkD2X4Bdz)
plugin : /usr/lib/ladspa/mbeq_1198.so\
device : equal1
#### /etc/asound.conf
```
ctl.equal {
	type equal
}

pcm.plugequal {
  type equal
  slave.pcm "plughw:0,0"
  # slave.pcm "plug:dmix"
}

pcm.equal{
  type plug
  slave.pcm plugequal
}

ctl.equal1 {
	type equal
	library "/usr/lib/ladspa/mbeq_1198.so"
	module "mbeq"
}

pcm.plugequal1 {
  type equal
  slave.pcm "plughw:0,0"
  # slave.pcm "plug:dmix"
  library "/usr/lib/ladspa/mbeq_1198.so"
  module "mbeq"
}

pcm.equal1{
  type plug
  slave.pcm plugequal1
}

pcm.dsp0 {
  type plug
  slave.pcm "eq"
}

pcm.eq {
    type ladspa
    slave.pcm "plughw:0,0"
    plugins [
	{
	    label mbeq
	    id 1198
	    # The following setting is customing bands.
	    input {
		controls  [-5 -5 -5 -5 -5 -5 ]
	    }
	}
    ]
}

audio_output {
        type "alsa"
        #device "hw:0,0"
        device "equal1"  
}
```
#### /etc/mpd.conf
```
# Volumio MPD Configuration File

# Files and directories #######################################################
music_directory		"/var/lib/mpd/music"
playlist_directory		"/var/lib/mpd/playlists"
db_file			"/var/lib/mpd/tag_cache"
#log_file			"/var/log/mpd/mpd.log"
#pid_file			"/var/run/mpd/pid"
#state_file			"/var/lib/mpd/state"
#sticker_file                   "/var/lib/mpd/sticker.sql"
###############################################################################

# General music daemon options ################################################
user				"mpd"
group                          "audio"
bind_to_address		"any"
#port				"6600"
#log_level			"default"
gapless_mp3_playback			"no"
#save_absolute_paths_in_playlists	"no"
#metadata_to_use	"artist,album,title,track,name,genre,date,composer,performer,disc"
auto_update    "yes"
#auto_update_depth "3"
###############################################################################
# Symbolic link behavior ######################################################
follow_outside_symlinks	"yes"
follow_inside_symlinks		"yes"
###############################################################################
# Input #######################################################################
#
input {
        plugin "curl"
#       proxy "proxy.isp.com:8080"
#       proxy_user "user"
#       proxy_password "password"
}
###############################################################################

# Decoder ################################################################

decoder { 
plugin "ffmpeg"
enabled "yes"
analyzeduration "1000000000"
probesize "1000000000"
}

###############################################################################

# Audio Output ################################################################

resampler {      
  		plugin "soxr"
  		quality "high"
  		threads "0"
}

audio_output {
		type		"alsa"
		name		"alsa"
#		device		"hw:0,0"    //原本使用HiFiBerry DAC+
		device "equal1"        //現在透過device equal1使用plugin mbeq_1198 
		dop			"no"
}

audio_output {
    type            "fifo"
    enabled         "no"
    name            "multiroom"
    path            "/tmp/snapfifo"
    format          "44100:16:2"
}

#replaygain			"album"
#replaygain_preamp		"0"
volume_normalization		"no"
###############################################################################

# MPD Internal Buffering ######################################################
audio_buffer_size		"8192"
buffer_before_play		"10%"
###############################################################################

# Resource Limitations ########################################################
#connection_timeout		"60"
max_connections			"20"
max_playlist_length		"32384"
max_command_list_size		"8192"
max_output_buffer_size		"16384"
###############################################################################

# Character Encoding ##########################################################
filesystem_charset		"UTF-8"
id3v1_encoding			"UTF-8"
###############################################################################
```
#### 用MPD開啟調整頁面
```
$ sudo -u mpd alsamixer -D equal1
```
如果ssh出現wrong lenth
Volumio播放顯示無法開啟ALSA : Operation permission denied
->砍掉.alsaequal.bin
```
$ sudo rm -rf /var/lib/mpd/.alsaequal.bin
$ rm ~/.alsaequal.bin
```
---
## Music Genre Classification
### 環境安裝
#### python
```
pip install PyQt5
pip install spyder
pip install scipy
```
#### MATLAB [toolbox](http://mirlab.org/jang/books/audiosignalprocessing/appNote/musicGenreClassification/html/goTutorial.html)
R2017a
* utility
* sap
* machineLearning
* asr
#### [libsvm](https://www.csie.ntu.edu.tw/~cjlin/libsvm/index.html)
*（在win和python皆為64位元的環境中）*
解壓縮->把所有所需檔案放進其中的python資料夾內（和svm.py、svmutil.py在同個路徑下）就可以正常使用
#### [GTZAN Genre Collection](http://opihi.cs.uvic.ca/sound/genres.tar.gz) dataset 
