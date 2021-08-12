embed -footer "for my love IkariYun#0024"
<drac2>
# from Desternia.FakeTestingStuff import *
pargs, returnstr, thing = argparse(&ARGS&), "", "something" if "%*%" == "" else "%*%"

defaultPFList = ["https://media.giphy.com/media/5PhDdJQd2yG1MvHzJ6/giphy.gif",
                 "https://media.giphy.com/media/jyPgrG8iqMu6Da7RWb/giphy.gif",
                 "https://media.giphy.com/media/4EEIsDmNJCiNcvAERe/giphy.gif",
                 "https://media.giphy.com/media/xCyjMEYF9H2ZcLqf7t/giphy.gif",
                 "https://media.giphy.com/media/JtNCrrdI19cAwECLUO/giphy.gif",
                 "https://media.giphy.com/media/kGnlAdc17XgxTyPmS3/giphy.gif",
                 "https://media.giphy.com/media/O5BvwlZzMNasU/giphy.gif"
                 ]

randGIF=randint(len(defaultPFList)-1)
returnstr += f'-title "{name} Fucking Yeets a {thing}!" -image {defaultPFList[randGIF]}'
return returnstr
</drac2>