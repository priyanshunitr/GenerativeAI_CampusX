from langchain_community.document_loaders import WebBaseLoader

url = "https://www.flipkart.com/dell-se-series-60-96-cm-24-inch-full-hd-ips-panel-hdr-10-300nits-1000-1-contrast-99-srgb-tilt-2-hdmi-2-1-tdms-supports-vrr-dp-1-4-3side-narrow-bezels-gaming-monitor-se2425hg/p/itm348286335e681?pid=MONHE5DMPX26HFVR&lid=LSTMONHE5DMPX26HFVRW3J6X1&marketplace=FLIPKART&store=6bo%2Fg0i%2F9no&spotlightTagId=default_TrendingId_6bo%2Fg0i%2F9no&srno=b_1_12&otracker=browse&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L2_view-all&fm=organic&iid=c921085d-7070-4182-b66f-7cec16814a45.MONHE5DMPX26HFVR.SEARCH&ppt=browse&ppn=browse&ssid=utm6lepgyo0000001765807358665"

loader = WebBaseLoader(url)

docs = loader.load()

print(docs)