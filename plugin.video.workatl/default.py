import xbmcaddon, util

addon = xbmcaddon.Addon('plugin.video.workatl')

util.playMedia(addon.getAddonInfo('name'), addon.getAddonInfo('icon'), 
               'http://phx2.vixtream.net/vcdnedge1/_definst_/ebstv_3/playlist.m3u8?wtCustomIp=73184830&wtendtime=1451806155&wthash=MasEyiyL5urXdhDPkWU9Xh7WwamwTUyjQ6hMM66uLg4= playpath=f24_livefr app=france24_live/fr')