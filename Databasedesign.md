Surah List DB
    SurahID
    name
    Arabic Name
    total Ayat
    meaningID(foriegn)
    total Leters
    abjad_no
    verifyID(foriegn)
    pageID(foriegn)

Ayat
    ayatID
    ayatno
    abjad_no
    SurahID(foriegn)
    meaningID(foriegn)
    ayatText
    verifyID(foriegn)
    pageID(foriegn)


rootWord
    ayatID(foriegn)
    rootWordID
    word
    tpye(ism,fail,harf)
    abjad_no
    rootWord
    meaningID(foriegn)
    count(like mahina 12 times)
    count word till Ayat start
    count word till Ayat end
    index no in Ayat
    WordDifferntforms(wordIDs)
    verifyID(foriegn)
    pageID(foriegn)

Word
    ayatID(foriegn)
    wordID
    Word
    MeaningID(foriegn)
    type(ism,fail,harf and thier subtypes [to understand arabicabrivations])
    abjad_no
    rootWord(foriegn)
    LinkedWord
    totalLeters
    verifyID(foriegn)
    pageID(foriegn)

Meaning
    MeaningID
    MeaningInEnglish
    MeaningInUrdu
    (otherLangs for later)
    verifyID(foriegn)


Page
    pageID
    pageIndex
    pageLink
    Poster(userID)
    Verify(foriegn)

Tag
    tagID
    tagName
    tagLink
    pageID(foriegn)

Verification
    verifyID
    Verifier1(userID)
    Verifier2(userID)
    Verifier3(userID)
    verifyDate
    status(pending,underreview,processed)


Feedback
    FeedbackID
    report
    userID(foriegn)
    pageID

User
    userID
    Username
    name
    email
    password(shah256)
    phoneNo
    Field
    Tags()
    Bio
    pageID(foriegn)
    LinkedData(for Later)

DistanceOfWord(earth and sirus)
    wordID
    2wordID
    wordcount
    LetterCount
    pageID(foriegn)

RingComposition(ayats)
    RingID
    ayatID
    RingID(forienKey)
    pageID(foriegn)


RingComposition(ayat Subparts)  like Ayat ul Kursi
    RingID
    ayatID
    subpartLengthofChars
    startWordIndex
    RingID(forienKey)
    pageID(foriegn)
