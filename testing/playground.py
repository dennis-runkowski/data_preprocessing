from data_preprocessing.base import DataPreprocess

        # "name": "data_loader",
        # "type": "csv",
        # "file_path": "/home/dennis_ubuntu/GitHub/data_preprocessing/testing/fake_job_postings.csv",
        # "columns": {"id": "job_id", "data": "description"},
        # "batch_size": 500,
        # "log_level": "DEBUG"


config = {
    "data": {
        "name": "data_loader",
        "type": "csv",
        "batch_size": 5,
        "log_level": "INFO"
    },
    "steps": [
        {
            "name": "normalize_text",
            "type": "lowercase",
            "log_level": "INFO"
        },
        {
            "name": "normalize_text",
            "type": "remove_digits",
            "log_level": "INFO"
        },
        {
            "name": "normalize_text",
            "type": "remove_html",
            "log_level": "INFO"
        },
        {
            "name": "normalize_text",
            "type": "lemmatizer",
            "log_level": "INFO"
        },
        {
            "name": "normalize_text",
            "type": "remove_punctuation",
            "log_level": "INFO"
        },
        {
            "name": "normalize_text",
            "type": "remove_stopwords",
            "options": "long_list",
            "log_level": "INFO"
        },
        {
            "name": "normalize_text",
            "type": "remove_whitespace",
            "log_level": "INFO"
        }
    ]
}

data = [
  {
    "id": 1,
    "data": "films adapted from comic books have had plenty of success , whether they're about superheroes ( batman , superman , spawn ) , or geared toward kids ( casper ) or the arthouse crowd ( ghost world ) , but there's never really been a comic book like from hell before . "
  },
  {
    "id": 2,
    "data": "for starters , it was created by alan moore ( and eddie campbell ) , who brought the medium to a whole new level in the mid '80s with a 12-part series called the watchmen . "
  },
  {
    "id": 3,
    "data": "to say moore and campbell thoroughly researched the subject of jack the ripper would be like saying michael jackson is starting to look a little odd . "
  },
  {
    "id": 4,
    "data": "the book ( or ' graphic novel , ' if you will ) is over 500 pages long and includes nearly 30 more that consist of nothing but footnotes . "
  },
  {
    "id": 5,
    "data": "in other words , don't dismiss this film because of its source . "
  },
  {
    "id": 6,
    "data": "if you can get past the whole comic book thing , you might find another stumbling block in from hell's directors , albert and allen hughes . "
  },
  {
    "id": 7,
    "data": "getting the hughes brothers to direct this seems almost as ludicrous as casting carrot top in , well , anything , but riddle me this : who better to direct a film that's set in the ghetto and features really violent street crime than the mad geniuses behind menace ii society ? "
  },
  {
    "id": 8,
    "data": "the ghetto in question is , of course , whitechapel in 1888 london's east end . "
  },
  {
    "id": 9,
    "data": "it's a filthy , sooty place where the whores ( called ' unfortunates ' ) are starting to get a little nervous about this mysterious psychopath who has been carving through their profession with surgical precision . "
  },
  {
    "id": 10,
    "data": "when the first stiff turns up , copper peter godley ( robbie coltrane , the world is not enough ) calls in inspector frederick abberline ( johnny depp , blow ) to crack the case . "
  },
  {
    "id": 11,
    "data": "abberline , a widower , has prophetic dreams he unsuccessfully tries to quell with copious amounts of absinthe and opium . "
  },
  {
    "id": 12,
    "data": "upon arriving in whitechapel , he befriends an unfortunate named mary kelly ( heather graham , say it isn't so ) and proceeds to investigate the horribly gruesome crimes that even the police surgeon can't stomach . "
  },
  {
    "id": 13,
    "data": "i don't think anyone needs to be briefed on jack the ripper , so i won't go into the particulars here , other than to say moore and campbell have a unique and interesting theory about both the identity of the killer and the reasons he chooses to slay . "
  },
  {
    "id": 14,
    "data": "in the comic , they don't bother cloaking the identity of the ripper , but screenwriters terry hayes ( vertical limit ) and rafael yglesias ( les mis ? rables ) do a good job of keeping him hidden from viewers until the very end . "
  },
  {
    "id": 15,
    "data": "it's funny to watch the locals blindly point the finger of blame at jews and indians because , after all , an englishman could never be capable of committing such ghastly acts . "
  },
  {
    "id": 16,
    "data": "and from hell's ending had me whistling the stonecutters song from the simpsons for days ( ' who holds back the electric car/who made steve guttenberg a star ? ' ) . "
  },
  {
    "id": 17,
    "data": "don't worry - it'll all make sense when you see it . "
  },
  {
    "id": 18,
    "data": "now onto from hell's appearance : it's certainly dark and bleak enough , and it's surprising to see how much more it looks like a tim burton film than planet of the apes did ( at times , it seems like sleepy hollow 2 ) . "
  },
  {
    "id": 19,
    "data": "the print i saw wasn't completely finished ( both color and music had not been finalized , so no comments about marilyn manson ) , but cinematographer peter deming ( don't say a word ) ably captures the dreariness of victorian-era london and helped make the flashy killing scenes remind me of the crazy flashbacks in twin peaks , even though the violence in the film pales in comparison to that in the black-and-white comic . "
  },
  {
    "id": 20,
    "data": "oscar winner martin childs' ( shakespeare in love ) production design turns the original prague surroundings into one creepy place . "
  },
  {
    "id": 21,
    "data": "even the acting in from hell is solid , with the dreamy depp turning in a typically strong performance and deftly handling a british accent . "
  },
  {
    "id": 22,
    "data": "ians holm ( joe gould's secret ) and richardson ( 102 dalmatians ) log in great supporting roles , but the big surprise here is graham . "
  },
  {
    "id": 23,
    "data": "i cringed the first time she opened her mouth , imagining her attempt at an irish accent , but it actually wasn't half bad . "
  },
  {
    "id": 24,
    "data": "the film , however , is all good . "
  },
  {
    "id": 25,
    "data": "2 : 00 - r for strong violence/gore , sexuality , language and drug content "
  },
  {
      "id": 26,
      "data": """
            <article class="" role="article">
            <div class="entry-content"></div>
            <!-- /.entry-content -->
            <p>Welcome to Deep Dish from the Chicago Council on Global Affairs, a podcast going beyond the headlines on critical global issues. Each week, Council Vice President of Studies Brian T. Hanson sits down with guests to explore issues that transcend borders and transform how people, businesses, and governments engage the world.</p><h2>Subscribe</h2><ul><li><a href="https://itunes.apple.com/us/podcast/deep-dish-on-global-affairs/id1169079758?mt=2&amp;ls=1" target="_blank">Apple Podcasts</a></li><li><a href="http://subscribeonandroid.com/deepdishonglobalaffairs.libsyn.com/rss?org=1364&amp;lvl=100&amp;ite=1490&amp;lea=72826&amp;ctr=0&amp;par=1&amp;trk=">Android Subscibe</a></li><li><a href="https://play.google.com/music/m/Id3b6voaas34jz4k3t25ymqfagu?t=Deep_Dish_on_Global_Affairs">Google Play Music</a></li><li><a href="http://deepdishonglobalaffairs.libsyn.com/rss" target="_blank">RSS Feed</a></li><li><a href="https://deepdishonglobalaffairs.libsyn.com/" target="_blank">Podcast Page</a><br>&nbsp;</li></ul><p><iframe allowfullscreen="" height="360" mozallowfullscreen="" msallowfullscreen="" oallowfullscreen="" scrolling="no" src="//html5-player.libsyn.com/embed/destination/id/580051/height/360/theme/custom/autoplay/no/autonext/no/thumbnail/yes/preload/no/no_addthis/no/direction/backward/no-cache/true/render-playlist/yes/custom-color/07add9/" style="border: none" webkitallowfullscreen="" width="100%"></iframe></p>      <hr>
            </article>
        """
  }
]

processer = DataPreprocess(config)
count = 0
for batch in processer.process_data(data):
    # count = count + len(batch)
    # print(count)
    print(batch)
