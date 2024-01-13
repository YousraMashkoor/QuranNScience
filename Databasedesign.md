1. Surah List DB
   - SurahID
   - name
   - Arabic Name
   - total Ayat
   - meaningID(foriegn)
   - total Leters
   - abjad_no
   - verifyID(foriegn)
   - pageID(foriegn)

2. Ayat
   - ayatID
   - ayatno
   - abjad_no
   - SurahID(foriegn)
   - meaningID(foriegn)
   - ayatText
   - verifyID(foriegn)
   - pageID(foriegn)


3. rootWord
   - ayatID(foriegn)
   - rootWordID
   - word
   - tpye(ism,fail,harf)
   - abjad_no
   - rootWord
   - meaningID(foriegn)
   - count(like mahina 12 times)
    - count word till Ayat start
    - count word till Ayat end
    - index no in Ayat
    - WordDifferntforms(wordIDs)
    - verifyID(foriegn)
    - pageID(foriegn)

4. Word
    - ayatID(foriegn)
    - wordID
    - Word
    - MeaningID(foriegn)
    - type(ism,fail,harf and thier subtypes [to understand arabicabrivations])
    - abjad_no
    - rootWord(foriegn)
    - LinkedWord
    - totalLeters
    - verifyID(foriegn)
    - pageID(foriegn)

5. Meaning
    - MeaningID
    - MeaningInEnglish
    - MeaningInUrdu
    - (otherLangs for later)
    - verifyID(foriegn)


6. Page
    - pageID
    - pageIndex
    - pageLink
    - Poster(userID)
    - Verify(foriegn)

7. Tag
    - tagID
    - tagName
    - tagLink
    - pageID(foriegn)

8. Verification
    - verifyID
    - Verifier1(userID)
    - Verifier2(userID)
    - Verifier3(userID)
    - verifyDate
    - status(pending,underreview,processed)


9. Feedback
    - FeedbackID
    - report
    - userID(foriegn)
    - pageID

10. User
    - userID
    - Username
    - name
    - email
    - password(shah256)
    - phoneNo
    - Field
    - Tags()
    - Bio
    - pageID(foriegn)
    - LinkedData(for Later)

11. DistanceOfWord(earth and sirus)
    - wordID
    - 2wordID
    - wordcount
    - LetterCount
    - pageID(foriegn)

12. RingComposition(ayats)
    - RingID
    - ayatID
    - RingID(forienKey)
    - pageID(foriegn)


13. RingComposition(ayat Subparts)  like Ayat ul Kursi
    - RingID
    - ayatID
    - subpartLengthofChars
    - startWordIndex
    - RingID(forienKey)
    - pageID(foriegn)
