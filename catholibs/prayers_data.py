"""Bank of traditional Catholic prayers used as Catholibs 'games'.

Each prayer is public-domain/traditional text. One prayer == one game.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Prayer:
    id: str
    title: str
    text: str


PRAYERS: list[Prayer] = [
    Prayer(
        id="our_father",
        title="The Our Father",
        text=(
            "Our Father, who art in heaven, hallowed be thy name. "
            "Thy kingdom come, thy will be done, on earth as it is in heaven. "
            "Give us this day our daily bread, and forgive us our trespasses, "
            "as we forgive those who trespass against us. "
            "And lead us not into temptation, but deliver us from evil. Amen."
        ),
    ),
    Prayer(
        id="hail_mary",
        title="The Hail Mary",
        text=(
            "Hail Mary, full of grace, the Lord is with thee. "
            "Blessed art thou among women, and blessed is the fruit of thy womb, Jesus. "
            "Holy Mary, Mother of God, pray for us sinners, "
            "now and at the hour of our death. Amen."
        ),
    ),
    Prayer(
        id="glory_be",
        title="Glory Be (Doxology)",
        text=(
            "Glory be to the Father, and to the Son, and to the Holy Spirit. "
            "As it was in the beginning, is now, and ever shall be, "
            "world without end. Amen."
        ),
    ),
    Prayer(
        id="apostles_creed",
        title="The Apostles' Creed",
        text=(
            "I believe in God, the Father almighty, creator of heaven and earth. "
            "I believe in Jesus Christ, his only Son, our Lord, who was conceived "
            "by the Holy Spirit, born of the Virgin Mary, suffered under Pontius Pilate, "
            "was crucified, died, and was buried. He descended into hell. "
            "On the third day he rose again from the dead. He ascended into heaven, "
            "and is seated at the right hand of God the Father almighty. "
            "From there he will come to judge the living and the dead. "
            "I believe in the Holy Spirit, the holy catholic Church, "
            "the communion of saints, the forgiveness of sins, "
            "the resurrection of the body, and life everlasting. Amen."
        ),
    ),
    Prayer(
        id="nicene_creed",
        title="The Nicene Creed",
        text=(
            "We believe in one God, the Father, the Almighty, maker of heaven and earth, "
            "of all that is seen and unseen. We believe in one Lord, Jesus Christ, "
            "the only Son of God, eternally begotten of the Father, God from God, "
            "Light from Light, true God from true God, begotten, not made, "
            "of one Being with the Father. Through him all things were made. "
            "For us and for our salvation he came down from heaven, by the power "
            "of the Holy Spirit he became incarnate from the Virgin Mary, and was made man. "
            "For our sake he was crucified under Pontius Pilate, he suffered death "
            "and was buried, and on the third day he rose again in accordance with "
            "the Scriptures. He ascended into heaven and is seated at the right hand "
            "of the Father. He will come again in glory to judge the living and the dead, "
            "and his kingdom will have no end. We believe in the Holy Spirit, the Lord, "
            "the giver of life, who proceeds from the Father and the Son, who with "
            "the Father and the Son is worshipped and glorified, who has spoken "
            "through the Prophets. We believe in one holy catholic and apostolic Church. "
            "We acknowledge one baptism for the forgiveness of sins. We look for "
            "the resurrection of the dead, and the life of the world to come. Amen."
        ),
    ),
    Prayer(
        id="hail_holy_queen",
        title="Hail Holy Queen (Salve Regina)",
        text=(
            "Hail, holy Queen, Mother of mercy, our life, our sweetness, and our hope. "
            "To thee do we cry, poor banished children of Eve. "
            "To thee do we send up our sighs, mourning and weeping in this valley of tears. "
            "Turn then, most gracious advocate, thine eyes of mercy toward us, "
            "and after this our exile, show unto us the blessed fruit of thy womb, Jesus. "
            "O clement, O loving, O sweet Virgin Mary."
        ),
    ),
    Prayer(
        id="act_of_contrition",
        title="Act of Contrition",
        text=(
            "O my God, I am heartily sorry for having offended thee, "
            "and I detest all my sins because I dread the loss of heaven "
            "and the pains of hell, but most of all because they offend thee, my God, "
            "who art all good and deserving of all my love. "
            "I firmly resolve, with the help of thy grace, "
            "to sin no more and to avoid the near occasion of sin. Amen."
        ),
    ),
    Prayer(
        id="confiteor",
        title="Confiteor (I Confess)",
        text=(
            "I confess to almighty God, to blessed Mary ever Virgin, "
            "to blessed Michael the Archangel, to blessed John the Baptist, "
            "to the holy Apostles Peter and Paul, to all the Saints, and to you, brethren, "
            "that I have sinned exceedingly in thought, word, and deed, through my fault, "
            "through my fault, through my most grievous fault. Therefore I beseech "
            "blessed Mary ever Virgin, blessed Michael the Archangel, "
            "blessed John the Baptist, the holy Apostles Peter and Paul, all the Saints, "
            "and you, brethren, to pray for me to the Lord our God. Amen."
        ),
    ),
    Prayer(
        id="st_michael",
        title="Prayer to St. Michael the Archangel",
        text=(
            "Saint Michael the Archangel, defend us in battle. "
            "Be our protection against the wickedness and snares of the devil. "
            "May God rebuke him, we humbly pray, and do thou, "
            "O Prince of the heavenly host, by the power of God, "
            "cast into hell Satan and all the evil spirits "
            "who prowl about the world seeking the ruin of souls. Amen."
        ),
    ),
    Prayer(
        id="memorare",
        title="The Memorare",
        text=(
            "Remember, O most gracious Virgin Mary, that never was it known "
            "that anyone who fled to thy protection, implored thy help, "
            "or sought thy intercession was left unaided. "
            "Inspired by this confidence, I fly unto thee, O Virgin of virgins, my mother. "
            "To thee do I come, before thee I stand, sinful and sorrowful. "
            "O Mother of the Word Incarnate, despise not my petitions, "
            "but in thy mercy hear and answer me. Amen."
        ),
    ),
    Prayer(
        id="anima_christi",
        title="Anima Christi",
        text=(
            "Soul of Christ, sanctify me. Body of Christ, save me. "
            "Blood of Christ, inebriate me. Water from the side of Christ, wash me. "
            "Passion of Christ, strengthen me. O good Jesus, hear me. "
            "Within thy wounds hide me. Suffer me not to be separated from thee. "
            "From the malicious enemy defend me. In the hour of my death call me, "
            "and bid me come to thee, that with thy saints I may praise thee "
            "forever and ever. Amen."
        ),
    ),
    Prayer(
        id="angelus",
        title="The Angelus",
        text=(
            "The angel of the Lord declared unto Mary, and she conceived by the Holy Spirit. "
            "Behold the handmaid of the Lord, be it done unto me according to thy word. "
            "And the Word was made flesh, and dwelt among us. "
            "Pray for us, O holy Mother of God, that we may be made worthy "
            "of the promises of Christ. Pour forth, we beseech thee, O Lord, "
            "thy grace into our hearts, that we, to whom the incarnation of Christ "
            "was made known by the message of an angel, may by his passion and cross "
            "be brought to the glory of his resurrection. Amen."
        ),
    ),
    Prayer(
        id="regina_caeli",
        title="Regina Caeli (Queen of Heaven)",
        text=(
            "Queen of heaven, rejoice, alleluia. For he whom you did merit to bear, alleluia, "
            "has risen as he said, alleluia. Pray for us to God, alleluia. "
            "Rejoice and be glad, O Virgin Mary, alleluia. For the Lord has truly risen, alleluia. "
            "Let us pray. O God, who gave joy to the world through the resurrection "
            "of thy Son, our Lord Jesus Christ, grant, we beseech thee, that through "
            "the intercession of the Virgin Mary, his Mother, we may obtain the joys "
            "of everlasting life. Through the same Christ our Lord. Amen."
        ),
    ),
    Prayer(
        id="come_holy_spirit",
        title="Come, Holy Spirit",
        text=(
            "Come, Holy Spirit, fill the hearts of thy faithful, and enkindle in them "
            "the fire of thy love. Send forth thy Spirit, and they shall be created, "
            "and thou shalt renew the face of the earth. Let us pray. O God, "
            "who didst instruct the hearts of the faithful by the light of the Holy Spirit, "
            "grant us in the same Spirit to be truly wise, and ever to rejoice "
            "in his consolation. Through Christ our Lord. Amen."
        ),
    ),
    Prayer(
        id="divine_praises",
        title="The Divine Praises",
        text=(
            "Blessed be God. Blessed be his holy name. "
            "Blessed be Jesus Christ, true God and true man. "
            "Blessed be the name of Jesus. Blessed be his most Sacred Heart. "
            "Blessed be his most precious blood. Blessed be Jesus in the most holy sacrament of the altar. "
            "Blessed be the great Mother of God, Mary most holy. "
            "Blessed be her holy and immaculate conception. "
            "Blessed be God in his angels and in his saints."
        ),
    ),
    Prayer(
        id="grace_before_meals",
        title="Grace Before Meals",
        text=(
            "Bless us, O Lord, and these thy gifts, which we are about to receive "
            "from thy bounty, through Christ our Lord. Amen."
        ),
    ),
    Prayer(
        id="guardian_angel",
        title="Prayer to the Guardian Angel",
        text=(
            "Angel of God, my guardian dear, to whom God's love commits me here, "
            "ever this day be at my side, to light and guard, to rule and guide. Amen."
        ),
    ),
    Prayer(
        id="st_francis_peace",
        title="Prayer of St. Francis for Peace",
        text=(
            "Lord, make me an instrument of thy peace. Where there is hatred, let me sow love. "
            "Where there is injury, pardon. Where there is doubt, faith. "
            "Where there is despair, hope. Where there is darkness, light. "
            "Where there is sadness, joy. O divine master, grant that I may not so much "
            "seek to be consoled as to console, to be understood as to understand, "
            "to be loved as to love. For it is in giving that we receive, "
            "it is in pardoning that we are pardoned, and it is in dying "
            "that we are born to eternal life. Amen."
        ),
    ),
    Prayer(
        id="prayer_before_crucifix",
        title="Prayer Before a Crucifix",
        text=(
            "Behold, O kind and most sweet Jesus, I cast myself upon my knees in thy sight, "
            "and with the most fervent desire of my soul I pray and beseech thee "
            "to impress upon my heart lively sentiments of faith, hope, and charity, "
            "true repentance for my sins, and a firm purpose of amendment, "
            "while with deep affection and grief of soul I ponder within myself "
            "and mentally contemplate thy five most precious wounds. Amen."
        ),
    ),
    # -- Catholic Book of Prayers (Rev. Maurus FitzGerald) --
    Prayer(
        id="cbop_the_sign_of_the_cross",
        title="The Sign of the Cross",
        text=(
            "In the name of the Father, and of the Son, and of the Holy Spirit. Amen."
        ),
    ),
    Prayer(
        id="cbop_the_lord_s_prayer",
        title="The Lord's Prayer (I)",
        text=(
            "Our Father, Who art in heaven, hallowed be Thy name; Thy kingdom come, Thy will be done "
            "on earth as it is in heaven. Give us this day our daily bread, and forgive us our "
            "trespasses, as we forgive those who trespass against us; and lead us not into "
            "temptation, but deliver us from evil. Amen."
        ),
    ),
    Prayer(
        id="cbop_the_hail_mary",
        title="The Hail Mary (Catholic Book of Prayers)",
        text=(
            "Hail, Mary, full of grace! The Lord is with thee; blessed art thou among women, and "
            "blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners "
            "now and at the hour of our death. Amen."
        ),
    ),
    Prayer(
        id="cbop_glory_be_to_the_father",
        title="Glory Be to the Father",
        text=(
            
            "Glory be to the Father, and to the Son, and to the Holy Spirit. As it was in the "
            "beginning, is now, and will be forever. Amen."
        
        ),
    ),
    Prayer(
        id="cbop_the_apostles_creed",
        title="The Apostles' Creed (Catholic Book of Prayers, I)",
        text=(
            "I believe in God, the Father Almighty, Creator of heaven and earth; and in Jesus "
            "Christ, His only Son, Our Lord; Who was conceived by the Holy Spirit, born of the Virgin "
            "Mary, suffered under Pontius Pilate, was crucified, died and was buried. He descended "
            "into hell; the third day He arose again from the dead; He ascended into heaven, sitteth "
            "at the right hand of God, the Father Almighty; from thence He shall come to judge the "
            "living and the dead. I believe in the Holy Spirit, the Holy Catholic Church, the "
            "communion of saints, the forgiveness of sins, the resurrection of the body, and life "
            "everlasting. Amen. (This is the traditional version of the Apostles' Creed; the newer "
            "version is found on p. 50.)"
        ),
    ),
    Prayer(
        id="cbop_the_confiteor",
        title="The Confiteor",
        text=(
            "I confess to Almighty God, to blessed Mary ever Virgin, to blessed Michael the "
            "Archangel, to blessed John the Baptist, to the holy Apostles Peter and Paul, and to all "
            "the saints, that I have sinned exceedingly in thought, word and deed, through my fault, "
            "through my fault, through my most grievous fault. Therefore, I beseech blessed Mary ever "
            "Virgin, blessed Michael the Archangel, blessed John the Baptist, the holy Apostles Peter "
            "and Paul, and all the saints, to pray to the Lord our God for me. May Almighty God have "
            "mercy on me, forgive me my sins, and bring me to everlasting life. Amen. May the "
            "almighty and merciful Lord grant me pardon, absolution, and remission of all my sins. "
            "Amen."
        ),
    ),
    Prayer(
        id="cbop_an_act_of_faith",
        title="An Act of Faith",
        text=(
            "O my God, I firmly believe that You are one God in three Divine Persons, Father, Son, "
            "and Holy Spirit; I believe that Your Divine Son became Man, and died for our sins, and "
            "that He will come to judge the living and the dead. I believe these and all the truths "
            "which the Holy Catholic Church teaches because You have revealed them, Who can neither "
            "deceive nor be deceived."
        ),
    ),
    Prayer(
        id="cbop_an_act_of_hope",
        title="An Act of Hope",
        text=(
            "O my God, relying on Your almighty power and infinite mercy and promises, I hope to "
            "obtain pardon for my sins, the help of Your grace, and life everlasting, through the "
            "merits of Jesus Christ, my Lord and Redeemer."
        ),
    ),
    Prayer(
        id="cbop_an_act_of_love",
        title="An Act of Love",
        text=(
            "O my God, I love You above all things with my whole heart and soul, because You are "
            "all-good and worthy of all love. I love my neighbor as myself for the love of You. I "
            "forgive all who have injured me, and ask pardon of all whom I have injured."
        ),
    ),
    Prayer(
        id="cbop_act_of_contrition",
        title="Act of Contrition (Catholic Book of Prayers, I)",
        text=(
            "O my God, I am heartily sorry for having offended You, and I detest all my sins because "
            "of Your just punishments, but most of all because they offend You, my God, Who are "
            "all-good and deserving of all my love. I firmly resolve, with the help of Your grace, to "
            "sin no more and to avoid the unnecessary occasions of sin. Amen."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_the_holy_spirit",
        title="Prayer to the Holy Spirit",
        text=(
            "Come, Holy Spirit, fill the hearts of Your faithful and kindle in them the fire of Your "
            "love. Send forth Your Spirit, and they shall be created. And You shall renew the face of "
            "the earth. Let us pray. O God, Who did instruct the hearts of the faithful by the light "
            "of the Holy Spirit: grant that, by the gift of the same Spirit, we may be always truly "
            "wise, and ever rejoice in His consolation. Through Christ our Lord. Amen."
        ),
    ),
    Prayer(
        id="cbop_the_angelus",
        title="The Angelus (Catholic Book of Prayers)",
        text=(
            "The Angel of the Lord declared unto Mary. And she conceived of the Holy Spirit. Hail "
            "Mary, etc. Behold the handmaid of the Lord. Be it done unto me according to Your word. "
            "Hail Mary, etc. And the Word was made flesh. And dwelt among us. Hail Mary, etc. Pray "
            "for us, O holy Mother of God. That we may be made worthy of the promises of Christ. Let "
            "us pray. Pour forth, we beseech You, O Lord, Your grace into our hearts, that we to whom "
            "the Incarnation of Christ, Your Son, was made known by the message of an angel, may by "
            "His Passion and Cross be brought to the glory of His Resurrection, through the same "
            "Christ our Lord. Amen."
        ),
    ),
    Prayer(
        id="cbop_regina_caeli",
        title="Regina Caeli",
        text=(
            "(Said during Eastertide instead of the Angelus) Queen of heaven, rejoice, alleluia. For "
            "He Whom you merited to bear, alleluia. Has risen as He said, alleluia. Pray for us to "
            "God, alleluia. Rejoice and be glad, O Virgin Mary, alleluia. Because the Lord is truly "
            "risen, alleluia. Let us pray. O God, Who by the Resurrection of Your Son, our Lord Jesus "
            "Christ, granted joy to the whole world, grant, we beg You, that, through the "
            "intercession of the Virgin Mary, His Mother, we may attain the joys of eternal life. "
            "Through the same Christ our Lord. Amen."
        ),
    ),
    Prayer(
        id="cbop_hail_holy_queen",
        title="Hail, Holy Queen",
        text=(
            "Hail, Holy Queen, Mother of mercy, hail, our life, our sweetness, and our hope! To you "
            "do we cry, poor banished children of Eve! To you do we send up our sighs, mourning, and "
            "weeping in this vale of tears! Turn then, most gracious advocate, your eyes of mercy "
            "toward us; and after this, our exile, show unto us the blessed fruit of your womb, "
            "Jesus! O clement, O loving, O sweet Virgin Mary!"
        ),
    ),
    Prayer(
        id="cbop_blessing_before_meals",
        title="Blessing Before Meals",
        text=(
            "Bless us, O Lord, and these Your gifts, which we are about to receive from Your bounty, "
            "through Christ our Lord. Amen."
        ),
    ),
    Prayer(
        id="cbop_grace_after_meals",
        title="Grace After Meals",
        text=(
            "We give You thanks for all Your benefits, O Almighty God, Who live and reign forever. "
            "Amen. May the souls of the faithful departed, through the mercy of God, rest in peace. "
            "Amen."
        ),
    ),
    Prayer(
        id="cbop_act_of_spiritual_communion",
        title="Act of Spiritual Communion",
        text=(
            "My Jesus, I believe that You are in the Blessed Sacrament. I love You above all things, "
            "and I long for You in my soul. Since I cannot now receive You sacramentally, come at "
            "least spiritually into my heart. I know You have already come. I embrace You and unite "
            "myself entirely to You; never permit me to be separated from You."
        ),
    ),
    Prayer(
        id="cbop_offering_to_the_holy_trinity",
        title="Offering to the Holy Trinity",
        text=(
            "Most holy and adorable Trinity, one God in three Persons, I praise You and give You "
            "thanks for all the favors You have bestowed upon me. Your goodness has preserved me "
            "until now. I offer You my whole being and in particular all my thoughts, words and "
            "deeds, together with all the trials I may undergo this day. Give them Your blessing. May "
            "Your Divine Love animate them and may they serve Your greater glory. I make this morning "
            "offering in union with the Divine intentions of Jesus Christ Who offers himself daily in "
            "the holy Sacrifice of the Mass, and in union with Mary, His Virgin Mother and our "
            "Mother, who was always the faithful handmaid of the Lord. Glory be to the Father, and to "
            "the Son, and to the Holy Spirit. Amen."
        ),
    ),
    Prayer(
        id="cbop_for_divine_guidance_through_the_day",
        title="For Divine Guidance Through the Day",
        text=(
            "Lord, God Almighty, You have brought us safely to the beginning of this day. Defend us "
            "today by Your mighty power, that we may not fall into any sin, but that all our words "
            "may so proceed and all our thoughts and actions be so directed, as to be always just in "
            "your sight. Through Christ our Lord. Amen. Direct, we beg You, O Lord, our actions by "
            "Your holy inspirations, and carry them on by Your gracious assistance, that every prayer "
            "and work of ours may begin always with You, and through You be happily ended. Amen."
        ),
    ),
    Prayer(
        id="cbop_morning_offering",
        title="Morning Offering",
        text=(
            "O my God, I offer You all my prayers, works, and sufferings, in union with the Sacred "
            "Heart of Jesus, for the intentions for which He pleads and offers Himself in the Holy "
            "Sacrifice of the Mass, in thanksgiving for Your favors, in reparation for my offenses, "
            "and in humble supplication for my temporal and eternal welfare, for the conversion of "
            "sinners, and for the relief of the poor souls in purgatory. I wish to gain all the "
            "indulgences attached to the prayers I shall say and to the good works I shall perform "
            "this day."
        ),
    ),
    Prayer(
        id="cbop_another_morning_offering",
        title="Another Morning Offering",
        text=(
            "O Jesus, through the Immaculate Heart of Mary, I offer You my prayers, works, joys and "
            "sufferings of this day for all the intentions of Your Sacred Heart, in union with the "
            "Holy Sacrifice of the Mass throughout the world, in reparation for my sins, for the "
            "intentions of all our associates and in particular for all the intentions of this month "
            "(mention intention if known)."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_god_s_protection_and_christ_s_presence",
        title="Prayer for God's Protection and Christ's Presence",
        text=(
            "As I arise today, may the strength of God pilot me, the power of God uphold me, the "
            "wisdom of God guide me. May the eye of God look before me, the ear of God hear me, the "
            "word of God speak for me. May the hand of God protect me, the way of God lie before me, "
            "the shield of God defend me, the host of God save me. May Christ shield me today … "
            "Christ with me, Christ before me, Christ behind me, Christ in me, Christ beneath me, "
            "Christ above me, Christ on my right, Christ on my left, Christ when I lie down, Christ "
            "when I sit, Christ when I stand, Christ in the heart of everyone who thinks of me, "
            "Christ in the mouth of everyone who speaks of me, Christ in every eye that sees me, "
            "Christ in every ear that hears me. (St. Patrick)"
        ),
    ),
    Prayer(
        id="cbop_midafternoon_prayer",
        title="Midafternoon Prayer",
        text=(
            "O divine Savior, I transport myself in spirit to Mount Calvary to ask pardon for my "
            "sins, for it was because of humankind's sins that You chose to offer Yourself in "
            "sacrifice. I thank You for Your extraordinary generosity and I am also grateful to You "
            "for making me a child of Mary, Your Mother. Blessed Mother, take me under your "
            "protection. St. John, you took Mary under your care. Teach me true devotion to Mary, the "
            "Mother of God. May the Father, the Son, and the Holy Spirit be glorified in all places "
            "through the Immaculate Virgin Mary."
        ),
    ),
    Prayer(
        id="cbop_invocations",
        title="Invocations (I)",
        text=(
            "May the Holy Trinity be blessed. Christ conquers! Christ reigns! Christ commands! O "
            "Heart of Jesus, burning with love for us, inflame our hearts with love for You. O Heart "
            "of Jesus, I place my trust in You. O Heart of Jesus, all for You. Most Sacred Heart of "
            "Jesus, have mercy on us. Teach me to do Your will, because You are my God. (Psalm "
            "143:10) Most Sacred Heart of Jesus, have mercy on us. O Lord, increase our faith. (Luke "
            "17:5) Sweet Heart of Mary, be my salvation. Jesus, meek and humble of heart, make my "
            "heart like unto Thine. May the Most Blessed Sacrament be praised and adored forever. "
            "Pray for us, O Holy Mother of God, that we may be made worthy of the promises of Christ. "
            "Father, into Your hands I commend my spirit. (Luke 23:46; see Psalm 31:6) Merciful Lord "
            "Jesus, grant them everlasting peace. Queen conceived without original sin, pray for us. "
            "Holy Mother of God, Mary ever Virgin, intercede for us. Holy Mary, pray for us. My "
            "Jesus, mercy."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_the_blessed_trinity",
        title="Prayer to the Blessed Trinity",
        text=(
            "I adore You, my God, and I thank You for having created me, for having made me a "
            "Christian and preserved me this day. I love You with all my heart and I am sorry for "
            "having sinned against You, because You are infinite Love and infinite Goodness. Protect "
            "me during my rest and may Your love be always with me. Amen. Eternal Father, I offer You "
            "the Precious Blood of Jesus Christ in atonement for my sins and for all the intentions "
            "of our Holy Church. Holy Spirit, Love of the Father and the Son, purify my heart and "
            "fill it with the fire of Your Love, so that I may be a chaste Temple of the Holy Trinity "
            "and be always pleasing to You in all things. Amen."
        ),
    ),
    Prayer(
        id="cbop_plea_for_divine_help",
        title="Plea for Divine Help",
        text=(
            "Hear us, Lord, holy Father, almighty and eternal God; and graciously send Your holy "
            "angel from heaven to watch over, to cherish, to protect, to abide with, and to defend "
            "all who dwell in this house. Through Christ our Lord. Amen."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_jesus",
        title="Prayer to Jesus",
        text=(
            "Jesus Christ, my God, I adore You and I thank You for the many favors You have bestowed "
            "on me this day. I offer You my sleep and all the moments of this night, and I pray You "
            "to preserve me from sin. Therefore, I place myself in Your most sacred Side, and under "
            "the mantle of our Blessed Lady, my Mother. May the holy angels assist me and keep me in "
            "peace, and may Your blessing be upon me."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_the_home",
        title="Prayer for the Home",
        text=(
            "We beseech You, O Lord, to visit this home, and to drive far from it all the snares of "
            "the enemy: let Your holy angels dwell therein so as to preserve us in peace; and let "
            "your blessing be always upon us. Through Christ our Lord. Amen."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_the_guardian_angel",
        title="Prayer to the Guardian Angel (Catholic Book of Prayers)",
        text=(
            "Angel of God, my guardian dear, to whom His love entrusts me here, ever this night be "
            "at my side, to light and guard, to rule and guide. Amen."
        ),
    ),
    Prayer(
        id="cbop_invocation_to_jesus_mary_and_joseph",
        title="Invocation to Jesus, Mary, and Joseph",
        text=(
            "Jesus, Mary, Joseph, I give You my heart and my soul. Jesus, Mary, Joseph, assist me in "
            "my last agony. Jesus, Mary, Joseph, may I sleep and rest in peace with You."
        ),
    ),
    Prayer(
        id="cbop_the_introductory_rites",
        title="The Introductory Rites",
        text=(
            
            "Acts of prayer and penitence prepare us to meet Christ as he comes in Word and "
            "Sacrament. We gather in worship to celebrate our unity with him and with one another in "
            "faith. Mass begins with an entrance procession of the ministers to the sanctuary, during "
            "which a chant is sung or the Entrance Antiphon of the day is recited."
        
        ),
    ),
    Prayer(
        id="cbop_greeting_3_forms",
        title="Greeting (3 Forms)",
        text=(
            "Priest: In the name of the Father, and of the Son, and of the Holy Spirit. People: "
            "Amen. (a) Priest: The grace of our Lord Jesus Christ, and the love of God, and the "
            "communion of the Holy Spirit be with you all. People: And with your spirit. (b) Priest: "
            "Grace to you and peace from God our Father and the Lord Jesus Christ. People: And with "
            "your spirit. (c) Priest: The Lord be with you. People: And with your spirit."
        ),
    ),
    Prayer(
        id="cbop_the_penitential_act_3_forms",
        title="The Penitential Act (3 Forms)",
        text=(
            "(a) Priest and People: I confess to almighty God and to you, my brothers and sisters, "
            "that I have greatly sinned, in my thoughts and in my words, in what I have done and in "
            "what I have failed to do, And, striking their breast, they say: through my fault, "
            "through my fault, through my most grievous fault; Then they continue: therefore I ask "
            "blessed Mary ever-Virgin, all the Angels and Saints, and you, my brothers and sisters, "
            "to pray for me to the Lord our God. (b) Priest: Have mercy on us, O Lord. People: For we "
            "have sinned against you. Priest: Show us, O Lord, your mercy. People: And grant us your "
            "salvation. (c) Priest or other minister: You were sent to heal the contrite of heart: "
            "Lord, have mercy. People: Lord, have mercy. Priest or other minister: You came to call "
            "sinners: Christ, have mercy. People: Christ, have mercy. Priest or other minister: You "
            "are seated at the right hand of the Father to intercede for us: Lord, have mercy. "
            "People: Lord, have mercy. (Other invocations may be used.) Absolution At the end of any "
            "of the forms of the Penitential Act: Priest: May almighty God have mercy on us, forgive "
            "us our sins, and bring us to everlasting life. People: Amen."
        ),
    ),
    Prayer(
        id="cbop_kyrie",
        title="Kyrie",
        text=(
            "Unless included in the Penitential Act, the Kyrie is sung or said by all, with "
            "alternating parts for the choir or cantor and for the people. Lord, have mercy. Lord, "
            "have mercy. Christ, have mercy. Christ, have mercy. Lord, have mercy. Lord, have mercy."
        ),
    ),
    Prayer(
        id="cbop_gloria",
        title="Gloria",
        text=(
            "As the Church assembled in the Spirit, we praise and pray to the Father and the Lamb. "
            "Glory to God in the highest, and on earth peace to people of good will. We praise you, "
            "we bless you, we adore you, we glorify you, we give you thanks for your great glory, "
            "Lord God, heavenly King, O God, almighty Father. Lord Jesus Christ, Only Begotten Son, "
            "Lord God, Lamb of God, Son of the Father, you take away the sins of the world, have "
            "mercy on us; you take away the sins of the world, receive our prayer; you are seated at "
            "the right hand of the Father, have mercy on us. For you alone are the Holy One, you "
            "alone are the Lord, you alone are the Most High, Jesus Christ, with the Holy Spirit, in "
            "the glory of God the Father. Amen."
        ),
    ),
    Prayer(
        id="cbop_collect",
        title="Collect",
        text=(
            "Priest: Let us pray. The Priest and people pray silently for a while. Then the Priest "
            "says the Collect, which gives the theme of the particular celebration and asks God to "
            "help us. He concludes with the words: … for ever and ever. People: Amen."
        ),
    ),
    Prayer(
        id="cbop_the_liturgy_of_the_word",
        title="The Liturgy of the Word",
        text=(
            
            "The proclamation of God's Word is always centered on Christ, present through his Word. "
            "Old Testament writings prepare for him; New Testament books speak of him directly. All "
            "of scripture calls us to believe once more and to follow. After the reading we reflect "
            "upon God's words and respond to them."
        
        ),
    ),
    Prayer(
        id="cbop_readings_and_responsorial_psalm",
        title="Readings and Responsorial Psalm",
        text=(
            "At the end of the First Reading: Reader: The word of the Lord. People: Thanks be to "
            "God. The people repeat the response sung by the cantor the first time and then after "
            "each verse. At the end of the Second Reading: Reader: The word of the Lord. People: "
            "Thanks be to God."
        ),
    ),
    Prayer(
        id="cbop_alleluia_gospel_acclamation",
        title="Alleluia (Gospel Acclamation)",
        text=(
            
            "The people repeat the Alleluia after the cantor's Alleluia and then after the verse. "
            "During Lent one of the following invocations is used as a response instead of the "
            "Alleluia: (1) Glory and praise to you, Lord Jesus Christ! (2) Glory to you, Lord Jesus "
            "Christ, Wisdom of God the Father! (3) Glory to you, Word of God, Lord Jesus Christ! (4) "
            "Glory to you, Lord Jesus Christ, Son of the Living God! (5) Praise and honor to you, "
            "Lord Jesus Christ! (6) Praise to you, Lord Jesus Christ, King of endless glory! (7) "
            "Marvelous and great are your works, O Lord! (8) Salvation, glory, and power to the Lord "
            "Jesus Christ!"
        
        ),
    ),
    Prayer(
        id="cbop_gospel",
        title="Gospel",
        text=(
            
            "Deacon (or Priest): The Lord be with you. People: And with your spirit. Deacon (or "
            "Priest): A reading from the holy Gospel according to N. People: Glory to you, O Lord. At "
            "the end: Deacon (or Priest): The Gospel of the Lord. People: Praise to you, Lord Jesus "
            "Christ."
        
        ),
    ),
    Prayer(
        id="cbop_homily",
        title="Homily",
        text=(
            "God's Word is spoken again in the Homily. The Holy Spirit speaking through the lips of "
            "the preacher explains and applies today's biblical readings to the needs of this "
            "particular congregation. He calls us to respond to Christ through the life we lead."
        ),
    ),
    Prayer(
        id="cbop_profession_of_faith_creed",
        title="Profession of Faith (Creed)",
        text=(
            "As a people we express our acceptance of God's message in the Scriptures and the "
            "Homily. We summarize our faith by proclaiming a creed handed down from the early Church. "
            "All say the Profession of Faith on Sundays."
        ),
    ),
    Prayer(
        id="cbop_the_nicene_creed",
        title="The Nicene Creed (Catholic Book of Prayers)",
        text=(
            
            "I believe in one God, the Father almighty, maker of heaven and earth, of all things "
            "visible and invisible. I believe in one Lord Jesus Christ, the Only Begotten Son of God, "
            "born of the Father before all ages. God from God, Light from Light, true God from true "
            "God, begotten, not made, consubstantial with the Father; through him all things were "
            "made. For us men and for our salvation he came down from heaven, At the words that "
            "follow, up to and including and became man, all bow. and by the Holy Spirit was "
            "incarnate of the Virgin Mary, and became man. For our sake he was crucified under "
            "Pontius Pilate, he suffered death and was buried, and rose again on the third day in "
            "accordance with the Scriptures. He ascended into heaven and is seated at the right hand "
            "of the Father. He will come again in glory to judge the living and the dead and his "
            "kingdom will have no end. I believe in the Holy Spirit, the Lord, the giver of life, who "
            "proceeds from the Father and the Son, who with the Father and the Son is adored and "
            "glorified, who has spoken through the prophets. I believe in one, holy, catholic and "
            "apostolic Church. I confess one Baptism for the forgiveness of sins and I look forward "
            "to the resurrection of the dead and the life of the world to come. Amen."
        
        ),
    ),
    Prayer(
        id="cbop_the_apostles_creed_2",
        title="The Apostles' Creed (Catholic Book of Prayers, II)",
        text=(
            "I believe in God, the Father almighty, Creator of heaven and earth, and in Jesus "
            "Christ, his only Son, our Lord, At the words that follow, up to and including the Virgin "
            "Mary, all bow. who was conceived by the Holy Spirit, born of the Virgin Mary, suffered "
            "under Pontius Pilate, was crucified, died and was buried; he descended into hell; on the "
            "third day he rose again from the dead; he ascended into heaven, and is seated at the "
            "right hand of God the Father almighty; from there he will come to judge the living and "
            "the dead. I believe in the Holy Spirit, the holy catholic Church, the communion of "
            "saints, the forgiveness of sins, the resurrection of the body, and life everlasting. "
            "Amen."
        ),
    ),
    Prayer(
        id="cbop_the_universal_prayer_prayer_of_the_faithful",
        title="The Universal Prayer (Prayer of the Faithful)",
        text=(
            "As a priestly people we unite with one another to pray for today's needs in the Church "
            "and the world. After the Priest's introduction the Deacon or other minister sings or "
            "says the invocations. People: Lord, hear our prayer. (or other response, according to "
            "local custom) At the end the Priest says the concluding prayer: People: Amen."
        ),
    ),
    Prayer(
        id="cbop_the_liturgy_of_the_eucharist",
        title="The Liturgy of the Eucharist",
        text=(
            "Made ready by reflection on God's Word, we enter now into the eucharistic sacrifice "
            "itself, the Supper of the Lord. We celebrate the memorial which the Lord instituted at "
            "his Last Supper. We are God's new people, the redeemed brothers and sisters of Christ, "
            "gathered by him around his table. We are here to bless God and to receive the gift of "
            "Jesus' Body and Blood so that our faith and life may be transformed."
        ),
    ),
    Prayer(
        id="cbop_preparation_of_the_gifts",
        title="Preparation of the Gifts",
        text=(
            
            "The bread and wine for the Eucharist, with our gifts for the Church and the poor, are "
            "gathered and brought to the altar. We prepare our hearts by song or in silence as the "
            "Lord's table is being set."
        
        ),
    ),
    Prayer(
        id="cbop_preparation_of_the_bread",
        title="Preparation of the Bread",
        text=(
            "Blessed are you, Lord God of all creation, for through your goodness we have received "
            "the bread we offer you: fruit of the earth and work of human hands, it will become for "
            "us the bread of life. If there is no singing, the Priest may say this prayer aloud, and "
            "the people reply: People: Blessed be God for ever."
        ),
    ),
    Prayer(
        id="cbop_preparation_of_the_wine",
        title="Preparation of the Wine",
        text=(
            "By the mystery of this water and wine may we come to share in the divinity of Christ "
            "who humbled himself to share in our humanity. Blessed are you, Lord God of all creation, "
            "for through your goodness we have received the wine we offer you: fruit of the vine and "
            "work of human hands, it will become our spiritual drink. If there is no singing, the "
            "Priest may say this prayer aloud, and the people reply: People: Blessed be God for ever."
        ),
    ),
    Prayer(
        id="cbop_invitation_to_prayer",
        title="Invitation to Prayer",
        text=(
            
            "Priest: Pray, brethren (brothers and sisters), that my sacrifice and yours may be "
            "acceptable to God, the almighty Father. People: May the Lord accept the sacrifice at "
            "your hands for the praise and glory of his name, for our good and the good of all his "
            "holy Church. The Priest, speaking in our name, says the Prayer over the Offerings, "
            "asking the Father to bless and accept these offerings. People: Amen."
        
        ),
    ),
    Prayer(
        id="cbop_eucharistic_prayer",
        title="Eucharistic Prayer",
        text=(
            "We begin the eucharistic service of praise and thanksgiving, the center of the entire "
            "celebration, the central prayer of worship. We lift our hearts to God, and offer praise "
            "and thanks as the Priest addresses this prayer to the Father through Jesus Christ. "
            "Together we join Christ in his sacrifice, celebrating his memorial in the holy meal and "
            "acknowledging with him the wonderful works of God in our lives. Priest: The Lord be with "
            "you. People: And with your spirit. Priest: Lift up your hearts. People: We lift them up "
            "to the Lord. Priest: Let us give thanks to the Lord our God. People: It is right and "
            "just. The Priest says the Preface here."
        ),
    ),
    Prayer(
        id="cbop_holy_holy_holy",
        title="Holy, Holy, Holy",
        text=(
            "Priest and People: Holy, Holy, Holy Lord God of hosts. Heaven and earth are full of "
            "your glory. Hosanna in the highest. Blessed is he who comes in the name of the Lord. "
            "Hosanna in the highest."
        ),
    ),
    Prayer(
        id="cbop_memorial_acclamation",
        title="Memorial Acclamation",
        text=(
            "Priest: The mystery of faith. People: A. We proclaim your Death, O Lord, and profess "
            "your Resurrection until you come again. B. When we eat this Bread and drink this Cup, we "
            "proclaim your Death, O Lord, until you come again. C. Save us, Savior of the world, for "
            "by your Cross and Resurrection you have set us free."
        ),
    ),
    Prayer(
        id="cbop_great_amen",
        title="Great Amen",
        text=(
            "Priest: … for ever and ever. People: Amen."
        ),
    ),
    Prayer(
        id="cbop_the_communion_rite",
        title="The Communion Rite",
        text=(
            
            "To prepare for the paschal meal, to welcome the Lord, we pray for forgiveness and "
            "exchange a sign of peace. Before eating Christ's Body and drinking his Blood, we must be "
            "one with him."
        
        ),
    ),
    Prayer(
        id="cbop_the_lord_s_prayer_2",
        title="The Lord's Prayer (II)",
        text=(
            "The Priest asks the people to join him in the prayer that Jesus taught us. Priest and "
            "People: Our Father, who art in heaven, hallowed be thy name; thy kingdom come, thy will "
            "be done on earth as it is in heaven. Give us this day our daily bread, and forgive us "
            "our trespasses, as we forgive those who trespass against us; and lead us not into "
            "temptation, but deliver us from evil."
        ),
    ),
    Prayer(
        id="cbop_doxological_conclusion_and_acclamation",
        title="Doxological Conclusion and Acclamation",
        text=(
            "Priest: Deliver us, Lord, we pray, from every evil, graciously grant peace in our days, "
            "that, by the help of your mercy, we may be always free from sin and safe from all "
            "distress, as we await the blessed hope and the coming of our Savior, Jesus Christ. "
            "People: For the kingdom, the power and the glory are yours now and for ever."
        ),
    ),
    Prayer(
        id="cbop_sign_of_peace",
        title="Sign of Peace",
        text=(
            "The Priest says the prayer for peace: Lord Jesus Christ, who said to your Apostles: "
            "Peace I leave you, my peace I give you, look not on our sins, but on the faith of your "
            "Church, and graciously grant her peace and unity in accordance with your will. Who live "
            "and reign for ever and ever. People: Amen. Priest: The peace of the Lord be with you "
            "always. People: And with your spirit. Deacon (or Priest): Let us offer each other the "
            "sign of peace. The people exchange a sign of peace and charity, according to local "
            "custom."
        ),
    ),
    Prayer(
        id="cbop_breaking_of_the_bread",
        title="Breaking of the Bread",
        text=(
            
            "Then the following is sung or said: People: Lamb of God, you take away the sins of the "
            "world, have mercy on us. Lamb of God, you take away the sins of the world, have mercy on "
            "us. Lamb of God, you take away the sins of the world, grant us peace. The hymn may be "
            "repeated until the breaking of the bread is finished, but the last phrase is always: "
            "\"Grant us peace.\" Meanwhile the Priest breaks the host over the paten and places a small "
            "piece in the chalice, saying one of two possible prayers quietly."
        
        ),
    ),
    Prayer(
        id="cbop_reception_of_communion",
        title="Reception of Communion",
        text=(
            
            "The Priest genuflects, takes the host and, holding it slightly raised above the paten "
            "or above the chalice, while facing the people, says aloud: Priest: Behold the Lamb of "
            "God, behold him who takes away the sins of the world. Blessed are those called to the "
            "supper of the Lamb. Priest and People (once only): Lord, I am not worthy that you should "
            "enter under my roof, but only say the word and my soul shall be healed. Priest: The Body "
            "of Christ. Communicant: Amen. Priest: The Blood of Christ. Communicant: Amen. The "
            "Communion Chant or other appropriate song or hymn is sung while Communion is given to "
            "the faithful. If there is no singing, the Communion Antiphon is said. Then, in the "
            "Prayer after Communion, the Priest prays in our name that we may live the life of faith "
            "since we have been strengthened by Christ himself. Our Amen makes his prayer our own. "
            "Priest: Let us pray …. Through Christ our Lord. People: Amen."
               ),
    ),
    Prayer(
        id="cbop_the_concluding_rites",
        title="The Concluding Rites",
        text=(
            
            "We have heard God's Word and eaten the Body of Christ. Now it is time for us to leave, "
            "to do good works, to praise and bless the Lord in our daily lives."
        
        ),
    ),
    Prayer(
        id="cbop_blessing_and_dismissal",
        title="Blessing and Dismissal",
        text=(
            "Priest: The Lord be with you. People: And with your spirit. Priest: May almighty God "
            "bless you, the Father, and the Son, and the Holy Spirit. People: Amen. Deacon (or "
            "Priest): (a) Go forth, the Mass is ended. (b) Go and announce the Gospel of the Lord. "
            "(c) Go in peace, glorifying the Lord by your life. (d) Go in peace. People: Thanks be to "
            "God."
        ),
    ),
    Prayer(
        id="cbop_act_of_hope",
        title="Act of Hope",
        text=(
            "Good Jesus, in You alone I place all my hope. You are my salvation and my strength, the "
            "Source of all good. Through Your mercy, through Your Passion and Death, I hope to obtain "
            "the pardon of my sins, the grace of final perseverance and a happy eternity."
        ),
    ),
    Prayer(
        id="cbop_act_of_love",
        title="Act of Love (I)",
        text=(
            "Jesus, my God, I love You with my whole heart and above all things, because you are the "
            "one supreme Good and an infinitely perfect Being. You have given your life for me, a "
            "poor sinner, and in Your mercy You have even offered Yourself as food for my soul. My "
            "God, I love You. Inflame my heart to love You more."
        ),
    ),
    Prayer(
        id="cbop_act_of_contrition_2",
        title="Act of Contrition (Catholic Book of Prayers, II)",
        text=(
            "O my Savior, I am truly sorry for having offended You because You are infinitely good "
            "and sin displeases You. I detest all the sins of my life and I desire to atone for them. "
            "Through the merits of Your Precious Blood, wash from my soul all stain of sin, so that, "
            "cleansed in body and soul, I may worthily approach the Most Holy Sacrament of the Altar."
        ),
    ),
    Prayer(
        id="cbop_act_of_desire",
        title="Act of Desire",
        text=(
            "Jesus, my God and my all, my soul longs for You. My heart yearns to receive You in Holy "
            "Communion. Come, Bread of heaven and Food of angels, to nourish my soul and to rejoice "
            "my heart. Come, most lovable Friend of my soul, to inflame me with such love that I may "
            "never again be separated from You."
        ),
    ),
    Prayer(
        id="cbop_prayer_of_st_thomas_aquinas",
        title="Prayer of St. Thomas Aquinas (I)",
        text=(
            "Almighty and eternal God, I approach the sacrament of Your only-begotten Son, our Lord "
            "Jesus Christ. As a sick man I approach the physician of life; as a man unclean, I come "
            "to the fountain of mercy; blind, to the light of eternal brightness; poor and needy, to "
            "the Lord of heaven and earth. I beseech You, therefore, in Your boundless mercy, to heal "
            "my sickness, to wash away my defilements, to enlighten my blindness, to enrich my "
            "poverty, and to clothe my nakedness. Let me receive the Bread of angels, the King of "
            "kings, the Lord of lords, with such reverence and humility, such contrition and faith, "
            "such purpose and intention, as may help the salvation of my soul. Grant, I beseech You, "
            "that I may receive not only the Sacrament of the Body and Blood of our Lord, but also "
            "the whole grace and virtue of the Sacrament. O most indulgent God, grant me so to "
            "receive the Body of Your only-begotten Son, our Lord, Jesus Christ, which He took of the "
            "Virgin Mary, that I may be found worthy to be incorporated with His Mystical Body and "
            "numbered among His members. O most loving Father, grant that I may one day forever "
            "contemplate Him unveiled and face to face, Whom, on my pilgrimage, I receive under a "
            "veil, Your beloved Son, Who lives and reigns with You and the Holy Spirit, one God, "
            "forever and ever."
        ),
    ),
    Prayer(
        id="cbop_act_of_faith",
        title="Act of Faith",
        text=(
            "Jesus, I firmly believe that You are present within me as God and Man, to enrich my "
            "soul with graces and to fill my heart with the happiness of the blessed. I believe that "
            "You are Christ, the Son of the living God!"
        ),
    ),
    Prayer(
        id="cbop_act_of_adoration",
        title="Act of Adoration (I)",
        text=(
            "With deepest humility, I adore You, my Lord and God; You have made my soul Your "
            "dwelling place. I adore You as my Creator from Whose hands I came and with Whom I long "
            "to be happy forever."
        ),
    ),
    Prayer(
        id="cbop_act_of_love_2",
        title="Act of Love (II)",
        text=(
            "Dear Jesus, I love You with my whole heart, my whole soul, and with all my strength. "
            "May the love of Your own Sacred Heart fill my soul and purify it so that I may die to "
            "the world for love of You, as You died on the Cross for love of me. My God, You are all "
            "mine; grant that I may be all Yours in time and in eternity."
        ),
    ),
    Prayer(
        id="cbop_act_of_thanksgiving",
        title="Act of Thanksgiving",
        text=(
            "From the depths of my heart I thank You, dear Lord, for Your infinite kindness in "
            "coming to me. How good You are to me! With Your most holy Mother and all the angels, I "
            "praise Your mercy and generosity toward me, a poor sinner. I thank You for nourishing my "
            "soul with Your Sacred Body and Precious Blood. I will try to show my gratitude to You in "
            "the Sacrament of Your love, by obedience to Your holy commandments, by fidelity to my "
            "duties, by kindness to my neighbor and by an earnest endeavor to become like You in my "
            "daily conduct."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_christ_the_king",
        title="Prayer to Christ the King",
        text=(
            "O Christ Jesus, I acknowledge You as King of the universe. All that has been created "
            "has been made for You. Exercise upon me all Your rights. I renew my baptismal promises, "
            "renouncing Satan and all his works and pomps. I promise to live a good Christian life "
            "and to be diligent in furthering the interests and teachings of Almighty God and Your "
            "Church."
        ),
    ),
    Prayer(
        id="cbop_prayer_of_st_thomas_aquinas_2",
        title="Prayer of St. Thomas Aquinas (II)",
        text=(
            "I Give you thanks, Lord, holy Father, almighty and eternal God, who have been pleased "
            "to nourish me, a sinner and your unworthy servant, with the precious Body and blood of "
            "your Son, our Lord Jesus Christ: this through no merits of mine, but solely to the "
            "graciousness of your mercy. And I pray that this Holy Communion may not be for me an "
            "offense to be punished, but a saving plea for forgiveness. May it be for me the armor of "
            "faith, and the shield of good will. May it cancel my faults, destroy concupiscence and "
            "carnal passion, increase charity and patience, humility and obedience and all the "
            "virtues, may it be a firm defense against the snares of all my enemies, both visible and "
            "invisible, the complete calming of my impulses, both of the flesh and of the spirit, a "
            "firm adherence to you, the one true God, and the joyful completion of my life's course. "
            "And I beseech you to lead me, a sinner to that banquet beyond all telling, where you "
            "with your Son and Holy Spirit you are the true light of your Saints, fullness of "
            "satisfied desire, eternal gladness, consummate delight and perfect happiness. Through "
            "Christ our Lord."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_our_redeemer",
        title="Prayer to Our Redeemer",
        text=(
            "Soul of Christ, sanctify me. Body of Christ, save me. Water from the side of Christ, "
            "wash me. Blood of Christ, motivate me. Passion of Christ, strengthen me. O good Jesus, "
            "hear me. Within Your wounds hide me. Suffer me not to be separated from You. From the "
            "malignant enemy, defend me. At the hour of death, call me, And bid me come to You, That "
            "with Your saints I may praise You Forever and ever."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_jesus_christ_crucified",
        title="Prayer to Jesus Christ Crucified",
        text=(
            "Behold, O kind and most sweet Jesus, I cast myself upon my knees in Your sight, and "
            "with the most fervent desire of my soul I pray and beseech You that You would impress "
            "upon my heart lively sentiments of Faith, Hope, and Charity, with true repentance for my "
            "sins, and a firm desire of amendment, while with deep affection and grief of soul I "
            "ponder within myself and mentally contemplate Your five most precious wounds, having "
            "before my eyes that which David spoke in prophecy of You, O good Jesus: They have "
            "pierced my hands and feet; they have numbered all my bones. A plenary indulgence is "
            "granted on each Friday of Lent and Passiontide to the faithful, who after Communion "
            "piously recite the above prayer before an image of Christ crucified; on other days of "
            "the year the indulgence is partial."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_jesus_and_mary",
        title="Prayer to Jesus and Mary",
        text=(
            "O Jesus living in Mary, come and live in Your servants, in the spirit of Your holiness, "
            "in the fullness of Your power, in the perfection of Your ways, and in the truth of Your "
            "mysteries. Reign in us over all adverse power through Your Holy Spirit, and for the "
            "glory of the Father. Amen. Mary, I come to you with childlike confidence and earnestly "
            "beg you to take me under your powerful protection. Grant me a place in your loving "
            "motherly heart. I place my immortal soul into your hands and give you my own poor heart."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_st_joseph",
        title="Prayer to St. Joseph (I)",
        text=(
            "Guardian of virgins, and holy father Joseph, to whose faithful custody Christ Jesus, "
            "innocence itself, and Mary, Virgin of virgins, were committed: I beg you, by these dear "
            "pledges, Jesus and Mary, that, being preserved from all uncleanness, I may with spotless "
            "mind, pure heart and chaste body ever serve Jesus and Mary most chastely all the days of "
            "my life. Amen."
        ),
    ),
    Prayer(
        id="cbop_act_of_adoration_2",
        title="Act of Adoration (II)",
        text=(
            "We adore You, Most Holy Lord, Jesus Christ, here and in all the churches of the whole "
            "world, and we bless You because by Your holy Cross You have redeemed the world. Have "
            "mercy on us. (St. Francis of Assisi)"
        ),
    ),
    Prayer(
        id="cbop_prayer_of_adoration_and_petition",
        title="Prayer of Adoration and Petition",
        text=(
            "I adore You, O Jesus, true God and true Man, here present in the Holy Eucharist, as I "
            "humbly kneel before You and unite myself in spirit with all the faithful on earth and "
            "all the Saints in heaven. In heartfelt gratitude for so great a blessing, I love You, my "
            "Jesus, with my whole soul, for You are infinitely perfect and all worthy of my love. "
            "Give me the grace never more in any way to offend You. Grant that I may be renewed by "
            "Your Eucharistic presence here on earth and be found worthy to arrive with Mary at the "
            "enjoyment of Your eternal and blessed presence in heaven."
        ),
    ),
    Prayer(
        id="cbop_prayer_of_reparation",
        title="Prayer of Reparation",
        text=(
            "With that deep and humble feeling which the Faith inspires in me, O my God and Savior, "
            "Jesus Christ, true God and true Man, I love You with all my heart, and I adore You Who "
            "are hidden here. I do so in reparation for all the irreverences, profanations, and "
            "sacrileges which You receive in the most august Sacrament of the Altar. I adore You, O "
            "my God, but not so much as You are worthy to be adored. Please accept my good will and "
            "help me in my weakness. Would that I could adore You with that perfect worship which the "
            "angels in heaven are able to offer You. O Jesus, may You be adored, loved, and thanked "
            "by all people at every moment in this most holy Sacrament."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_today_s_needs",
        title="Prayer for Today's Needs",
        text=(
            "Lord, for tomorrow and its needs I do not pray; keep me, my God, from stain of sin, "
            "just for today. Let me both diligently work and duly pray; let me be kind in word and "
            "deed, just for today. Let me be slow to do my will, prompt to obey; help me to mortify "
            "my flesh, just for today. Let me no wrong or idle word unthinking say; set a seal upon "
            "my lips, just for today. Let me in season, Lord, be grave, in season gay; let me be "
            "faithful to Your grace, just for today. And if today my tide of life should ebb away, "
            "give me Your Sacraments divine, sweet Lord, today. So for tomorrow and its needs, I do "
            "not pray; but keep me, guide me, love me, Lord, just for today. Sister M. Xavier, S.N.D."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_bring_christ_into_our_day",
        title="Prayer to Bring Christ into Our Day",
        text=(
            "Lord Jesus, present before me in the Sacrament of the Altar, help me to cast out from "
            "my mind all thoughts of which You do not approve and from my heart all emotions which "
            "You do not encourage. Enable me to spend my entire day as a co-worker with You, carrying "
            "out the tasks that You have entrusted to me. Be with me at every moment of this day: "
            "during the long hours of work, that I may never tire or slacken from Your service; "
            "during my conversations, that they may not become for me occasions for meanness toward "
            "others; during the moments of worry and stress, that I may remain patient and "
            "spiritually calm; during periods of fatigue and illness, that I may avoid self-pity and "
            "think of others; during times of temptation, that I may take refuge in Your grace. Help "
            "me to remain generous and loyal to You this day and so be able to offer it all up to You "
            "with its successes which I have achieved by Your help and its failures which have "
            "occurred through my own fault. Let me come to the wonderful realization that life is "
            "most real when it is lived with You as the Guest of my soul."
        ),
    ),
    Prayer(
        id="cbop_invocations_2",
        title="Invocations (II)",
        text=(
            "Praise and adoration ever more be given to the most Holy Sacrament. O Sacrament most "
            "holy, O Sacrament divine! All praise and all thanksgiving be every moment Thine!"
        ),
    ),
    Prayer(
        id="cbop_down_in_adoration_falling",
        title="Down in Adoration Falling",
        text=(
            "Down in adoration falling, Lo! the sacred Host we hail; Lo! o'er ancient forms "
            "departing, Newer rites of grace prevail; Faith for all defects supplying, Where the "
            "feeble senses fail. To the everlasting Father, And the Son Who reigns on high, With the "
            "Holy Spirit proceeding Forth from each eternally, Be salvation, honor, blessing, Might "
            "and endless majesty. Amen. The minister then says a Prayer and concludes: For ever and "
            "ever. Amen."
        ),
    ),
    Prayer(
        id="cbop_the_divine_praises",
        title="The Divine Praises (Catholic Book of Prayers)",
        text=(
            "Blessed be God. Blessed be His holy Name. Blessed be Jesus Christ, true God and true "
            "Man. Blessed be the name of Jesus. Blessed be His most Sacred Heart. Blessed be His most "
            "Precious Blood. Blessed be Jesus in the most holy Sacrament of the altar. Blessed be the "
            "Holy Spirit, the Paraclete. Blessed be the great Mother of God, Mary most holy. Blessed "
            "be her holy and immaculate conception. Blessed be her glorious assumption. Blessed be "
            "the name of Mary, virgin and mother. Blessed be St. Joseph, her most chaste spouse. "
            "Blessed be God in His Angels and in His Saints."
        ),
    ),
    Prayer(
        id="cbop_meditation_on_the_eucharist",
        title="Meditation on the Eucharist",
        text=(
            "While they were eating He took bread, and after He had pronounced the blessing, He "
            "broke it and gave it to them, saying \"Take it; this is My Body.\" Then He took a cup, and "
            "after offering thanks He gave it to them. After they all drank from it, He said to them, "
            "\"This is My Blood of the Covenant, which will be shed on behalf of many. Amen, I say to "
            "you, from now on I shall not drink this fruit of the vine until the day when I shall "
            "drink it anew in the Kingdom of God\" (Mark 14:22-25)."
        ),
    ),
    Prayer(
        id="cbop_prayer_of_thanksgiving_and_petition",
        title="Prayer of Thanksgiving and Petition",
        text=(
            "We give you thanks, O Christ, our God; in Your goodness You have given us Your Body in "
            "this Sacrament to enable us to live holy lives. Through Your grace keep us pure and "
            "without stain. Remain in us to protect us. Direct our steps in the way of Your holy and "
            "benevolent will."
        ),
    ),
    Prayer(
        id="cbop_prayer_before_confession",
        title="Prayer Before Confession",
        text=(
            "My Lord and God, I have sinned. I am guilty before You. Grant me the strength to say to "
            "Your minister what I say to You in the secret of my heart. Increase my repentance. Make "
            "it more genuine. May it be really a sorrow for having offended You and my neighbor "
            "rather than a wounded love of self. Help me to atone for my sin. May the sufferings of "
            "my life and my little mortifications be joined with the sufferings of Jesus, Your Son, "
            "and cooperate in rooting sin from the world."
        ),
    ),
    Prayer(
        id="cbop_examination_of_conscience",
        title="Examination of Conscience",
        text=(
            "How long has it been since my last confession? Did I conceal any sin? Did I say my "
            "penance? Have I neglected my home and my family duties, or my work? Have I been lazy, "
            "neglectful, or willfully distracted during prayer or at Mass? Have I used God's name "
            "irreverently, or taken false or needless oaths? Have I missed Mass through my own fault "
            "on Sundays or holydays, or worked unnecessarily on Sunday? Have I disobeyed, angered, or "
            "been disrespectful toward my parents, teachers, employers, or other superiors? Have I "
            "been unjust and unkind to those over whom I have authority? Have I quarreled with or "
            "willfully hurt anyone? Have I been guilty of cruelty, mental or physical, toward anyone? "
            "Have I caused another to commit sin? Have I offended in any way by thought, word, or "
            "deed against purity? Have I led others into sin? Have I stolen or destroyed property "
            "belonging to any other person or company? Have I given a bad example to the members of "
            "my family or others? Have I knowingly accepted stolen goods? Have I paid all my just "
            "debts? Have I told lies, repeated harmful gossip, or injured another person's character? "
            "Have I been sinfully angry, greedy, proud, envious, jealous, or intemperate in eating or "
            "drinking? Have I willfully broken any of the Church laws concerning fast or abstinence? "
            "Have I failed to support my Church? Have I received Communion during Easter Time? For "
            "married people: Have I failed to show love, respect, and good example toward my partner? "
            "Have I neglected my duty to my children in regard to their religious instruction, to "
            "their training in good habits, and to their schooling? Have I sinned against the duties "
            "of married life? We must confess the number of our sins as best we can remember them."
        ),
    ),
    Prayer(
        id="cbop_1_reception_of_the_penitent",
        title="1. Reception of the Penitent",
        text=(
            "Penitent: In the name of the Father, and of the Son, and of the Holy Spirit. Amen. "
            "Priest: May the grace of the Holy Spirit fill your heart with light, that you may "
            "confess your sins with loving trust and come to know that God is merciful. Penitent: "
            "Amen."
        ),
    ),
    Prayer(
        id="cbop_2_reading_of_the_word_of_god",
        title="2. Reading of the Word of God",
        text=(
            "Priest: After John had been arrested, Jesus came to Galilee proclaiming the Gospel of "
            "God: \"This is the time of fulfillment. The kingdom of God is at hand! Repent and believe "
            "in the Gospel.\" (Mark 1:14-15). (Another reading may be used.)"
        ),
    ),
    Prayer(
        id="cbop_3_confession_of_sins",
        title="3. Confession of Sins",
        text=(
            "The penitent confesses his sins; the priest accepts the confession and imposes a "
            "penance. The penitent then expresses sorrow for sins in these or similar words: "
            "Penitent: My God, I am sorry for my sins with all my heart. In choosing to do wrong and "
            "failing to do good, I have sinned against you whom I should love above all things. I "
            "firmly intend, with your help, to do penance, to sin no more, and to avoid whatever "
            "leads me to sin. Our Savior Jesus Christ suffered and died for us. In his name, my God, "
            "have mercy."
        ),
    ),
    Prayer(
        id="cbop_4_absolution",
        title="4. Absolution",
        text=(
            "Priest: God, the Father of mercies, through the death and resurrection of his Son, has "
            "reconciled the world to himself and sent the Holy Spirit among us for the forgiveness of "
            "sins; through the ministry of the Church may God give you pardon and peace, and I "
            "absolve you from your sins in the name of the Father, and of the Son, and of the Holy "
            "Spirit. Amen."
        ),
    ),
    Prayer(
        id="cbop_5_proclamation_of_praise_of_god_and_dismissal",
        title="5. Proclamation of Praise of God and Dismissal",
        text=(
            "Priest: Give thanks to the Lord, for he is good. Penitent: His mercy endures for ever."
        ),
    ),
    Prayer(
        id="cbop_thanksgiving_after_confession",
        title="Thanksgiving After Confession",
        text=(
            "My dearest Jesus, I have told all my sins as well as I could. I have tried hard to make "
            "a good confession. I feel sure that You have forgiven me. I thank You. It is only "
            "because of all Your sufferings that I can go to confession and free myself from my sins. "
            "Your Heart is full of love and mercy for poor sinners. I love You because You are so "
            "good to me. My loving Savior, I shall try to keep from sin and to love You more each "
            "day. My dear Mother Mary, pray for me and help me to keep my promises. Protect me and do "
            "not let me fall back into sin."
        ),
    ),
    Prayer(
        id="cbop_prayer_in_praise_of_the_trinity",
        title="Prayer in Praise of the Trinity",
        text=(
            "I venerate and glorify You, O most Blessed Trinity, in union with that ineffable glory "
            "with which God the Father, in His omnipotence, honors the Holy Spirit forever. I magnify "
            "and bless You, O most Blessed Trinity, in union with that most reverent glory with which "
            "God the Son, in His ineffable wisdom, glorifies the Father and the Holy Spirit forever. "
            "I adore and extol You, O most Blessed Trinity, in union with that most adequate and "
            "befitting glory with which the Holy Spirit, in His unchangeable goodness, extols the "
            "Father and the Son forever."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_be_conformed_to_the_divine_will",
        title="Prayer to Be Conformed to the Divine Will",
        text=(
            "Most holy Trinity, Godhead indivisible, Father, Son, and Holy Spirit, our first "
            "beginning and our last end, You have made us in accord with your own image and likeness. "
            "Grant that all the thoughts of our minds, all the words of our tongues, all the "
            "affections of our hearts, and all the actions of our being may always be conformed to "
            "Your holy will. Thus, after we have seen You here below in creation and in a dark manner "
            "by means of faith, we may come at last to contemplate You face-to-face forever in "
            "heaven."
        ),
    ),
    Prayer(
        id="cbop_prayer_of_consecration_to_the_trinity",
        title="Prayer of Consecration to the Trinity",
        text=(
            "O God, I vow and consecrate to You all that is in me: my memory and my actions to God "
            "the Father; my understanding and my words to God the Son; my will and my thoughts to God "
            "the Holy Spirit; my heart and my body, my tongue, my senses, and all my sorrows to the "
            "sacred humanity of Jesus Christ, Who was content to be betrayed into the hands of wicked "
            "men and to suffer the torment of the Cross. St. Francis de Sales"
        ),
    ),
    Prayer(
        id="cbop_prayer_of_praise_and_petition",
        title="Prayer of Praise and Petition",
        text=(
            "We praise You, invisible Father, giver of immortality, and source of life and light. "
            "You love all human beings, especially the poor. You seek reconciliation with all of them "
            "and You draw them to yourself by sending Your beloved Son to visit them. Make us really "
            "alive by giving us the light to know You, the only true God, and Jesus Christ Whom You "
            "have sent. Grant us the Holy Spirit and enable us to speak volumes about Your ineffable "
            "mysteries. St. Serapion of Thmuis"
        ),
    ),
    Prayer(
        id="cbop_prayer_to_the_father_for_the_benefits_of_christ_s_redemption",
        title="Prayer to the Father for the Benefits of Christ's Redemption",
        text=(
            "Eternal Father, I offer You the infinite satisfaction which Jesus rendered to your "
            "justice in behalf of sinners on the tree of the Cross. I ask that You would make "
            "available the merits of His Precious Blood to all guilty souls to whom sin has brought "
            "death. May they rise again to the life of grace and glorify You forever."
        ),
    ),
    Prayer(
        id="cbop_prayer_of_thanks_for_the_father_s_love",
        title="Prayer of Thanks for the Father's Love",
        text=(
            "Eternal Father, we thank You for Your great love. You give the world the best of "
            "Yourself, the mirror of Your perfect transparency, the splendor of Your very being—Your "
            "Son Jesus. We thank You for giving Jesus to us as our Savior, not as a tyrant but as a "
            "friend, not as a superior but as a brother. Help us to open our hearts to His light "
            "without fear of being overwhelmed but exultant with the joy that comes from this light "
            "upon all who accept it with gladness."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_the_father_for_reconciliation",
        title="Prayer to the Father for Reconciliation",
        text=(
            "Heavenly Father, in the death and resurrection of Jesus Christ Your Son You willed to "
            "reconcile all mankind to Yourself and so to reconcile all human beings with each other "
            "in peace. Hear the prayer of Your people. Let Your spirit of life and holiness renew us "
            "in the depths of our being and unite us throughout our life to the risen Christ: for He "
            "is our Brother and Savior. With all Christians we seek to follow the way of the Gospel. "
            "Keep us faithful to the teachings of the Church and alive to the needs of our neighbors. "
            "Give us strength to work for reconciliation, unity, and peace. May those who seek the "
            "God they do not yet know discover in You the source of light and hope. May those who "
            "work for others find strength in You. May those who already know You seek even further "
            "and experience the depths of Your love. Forgive us our sins, deepen our faith, kindle "
            "our hope, and enliven our hearts with love. May we walk in the footsteps of Jesus as "
            "Your beloved sons and daughters. With the help of Mary, our Mother, may Your Church be "
            "the sign and sacrament of salvation for all people, that the world may believe in Your "
            "love and Your truth."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_jesus_true_man",
        title="Prayer to Jesus, True Man",
        text=(
            "O Jesus, You are true Man. You took upon Yourself a human body and soul, You thought "
            "with a human mind, and You acted through a human will. But You are far above every other "
            "human. No one ever spoke like You, with such authority, freedom, and gentleness, "
            "indicating the paths of love, justice, and sincerity. And no one ever matched Your "
            "teachings. You spoke about the mystery of God in a way so elevated above others that You "
            "make it possible for us to come to know God and achieve a living love for Him. O Jesus, "
            "no one ever acted like You, either. You left us an example of the perfect human life: by "
            "Your preference for poverty, by Your love for the poor and the sick, by Your concern for "
            "the suffering, by Your liberating message of salvation, by Your espousal of peace and "
            "service, by Your obedience to the Father—even to the death of the Cross. O Jesus, help "
            "us to know You more. Help us to live with You so that we may live fully human lives. "
            "Satisfy us with Yourself, the Man for others, and with God, perfect Love—the "
            "Man-Who-is-Love, and God-Who-is-Love."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_jesus_true_god",
        title="Prayer to Jesus, True God",
        text=(
            "O Jesus, You are the Son of God. You resolve our problems and respond to our "
            "aspirations with unexpected fullness. As the Son sent to us by the Father, You are the "
            "God Who comes to meet us and manifests for us the God Whom we seek. You are the "
            "revelation of God for us—the full, perfect, and definitive revelation—God in person. In "
            "You the God-Who-is-far-off becomes the God-Who-is-near, the God-with-us, and the "
            "God-Who-is-one-of-us, our companion of life's journey. You alone, O Lord, are the Way, "
            "the Truth, and the Life, the Messiah, and the Son of the living God."
        ),
    ),
    Prayer(
        id="cbop_petitions_to_jesus",
        title="Petitions to Jesus",
        text=(
            "O good Jesus: Word of the eternal Father, convert me. Son of Mary, take me as her "
            "child. My Master, teach me. Prince of peace, give me peace. My Refuge, receive me. My "
            "Shepherd, feed my soul. Model of patience, comfort me. Meek and humble of heart, help me "
            "to become like You. My Redeemer, save me. My God and my All, possess me. The true Way, "
            "direct me. Eternal Truth, instruct me. Life of the saints, make me live in You. My "
            "Support, strengthen me. My Justice, justify me. My Mediator with the Father, reconcile "
            "me. Physician of my soul, heal me. My Judge, pardon me. My King, rule me. My "
            "Sanctification, sanctify me. Abyss of goodness, pardon me. Living Bread of heaven, feed "
            "me. Father of the prodigal, receive me. Joy of my soul, be my only happiness. My Helper, "
            "assist me. Magnet of love, draw me. My Protector, defend me. My Hope, sustain me. Object "
            "of my love, unite me to Yourself. Fountain of life, refresh me. My Divine Victim, atone "
            "for me. My Last End, let me possess You. My Glory, glorify me."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_the_miraculous_infant_of_prague",
        title="Prayer to the Miraculous Infant of Prague",
        text=(
            "Dear Jesus, Little Infant of Prague, how tenderly You love us! Your greatest joy is to "
            "dwell among us and to bestow Your blessing upon us. So many who turned to You with "
            "confidence have received graces and had their petitions granted. I also come before You "
            "now with this special request (mention it). Dear Infant, rule over me and do with me and "
            "mine as You will, for I know that in Your divine wisdom and love You will arrange "
            "everything for the best. Do not withdraw Your hand from me, but protect me and bless me "
            "forever. Dear Infant, help me in my needs. Make me truly happy with You in time and in "
            "eternity, and I shall thank You forever with all my heart."
        ),
    ),
    Prayer(
        id="cbop_prayer_of_praise_to_the_holy_name_of_jesus",
        title="Prayer of Praise to the Holy Name of Jesus",
        text=(
            "O glorious Name of Jesus, gracious Name, Name of love and of power! Through You sins "
            "are forgiven, enemies are vanquished, the sick are freed from illness, the suffering are "
            "made strong and cheerful. You bring honor to those who believe, instruction to those who "
            "preach, strength to those who toil, and sustenance to those who are weary. Our love for "
            "You is ardent and glowing, our prayers are heard, the souls of those who contemplate You "
            "are filled to overflowing, and all the blessed in heaven are filled with Your glory. "
            "Grant that we too may reign with them through this Your most holy Name."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_the_crucified_christ",
        title="Prayer to the Crucified Christ",
        text=(
            "Lord Jesus hanging on the Cross, I raise sorrowful and shameful eyes to You. You have "
            "granted me untold blessings and I have repaid You by contributing to Your Passion and "
            "death. My hands took part in Your scourging, my voice was among those who denied You and "
            "called for Your death, my thoughts, brought about Your crowning with thorns, my sins "
            "drove the nails into Your hands and feet, and the lance into Your side. Dear Lord, "
            "forgive me for all these sins. You are great, glorious, and infinitely good; I am "
            "insignificant, selfish, and hopelessly sinful. But I am sorry for all my sins, and by "
            "the Blood shed in Your Passion I beg for forgiveness and for a share in Your love and "
            "grace."
        ),
    ),
    Prayer(
        id="cbop_prayer_of_the_seven_last_words",
        title="Prayer of the Seven Last Words",
        text=(
            "O divine Jesus, incarnate Son of God, for our salvation You consented to be born in a "
            "stable, to spend Your whole life amid poverty, trials, and misery, and to die surrounded "
            "by sufferings on the Cross. At the hour of my death, please say to Your Father: Father, "
            "forgive him/her. Say to Your beloved Mother: Behold your son/daughter. Say to my soul: "
            "This day you shall be with Me in paradise. My God, my God, do not forsake me in that "
            "hour. I thirst, yes, my soul thirsts for You Who are the fountain of living waters. My "
            "life passes away like a shadow; in a short while everything will be accomplished. "
            "Therefore my adorable Savior, from this moment and for all eternity into Your hands I "
            "commend my spirit. Lord Jesus, receive my soul."
        ),
    ),
    Prayer(
        id="cbop_prayer_in_honor_of_the_precious_blood",
        title="Prayer in Honor of the Precious Blood",
        text=(
            "Precious Blood of Jesus, infinite price of our redemption and both the drink and the "
            "laver of our souls, You continually plead the cause of all people before the throne of "
            "infinite mercy. From the depths of my heart I adore You. Jesus, insofar as I am able I "
            "want to make reparation for the insults and outrages which You receive from human "
            "beings, especially from those who blaspheme You. Who would not venerate this Blood of "
            "infinite value! Who does not feel inflamed with love for Jesus Who shed it! What would "
            "have become of me had I not been redeemed by this divine Blood! Who has drained it all "
            "from the veins of my Savior? Surely this was the work of love! O infinite love, which "
            "has given us this saving balm! O balm beyond all price, welling up from the fountain of "
            "infinite love! Grant that every heart and every tongue may render You praise and thanks "
            "now and forever!"
        ),
    ),
    Prayer(
        id="cbop_the_promises_of_the_sacred_heart",
        title="The Promises of the Sacred Heart",
        text=(
            "In various appearances to St. Margaret Mary Alacoque, Jesus manifested His great love "
            "for human beings and made the following promises to those who give particular honor to "
            "His Sacred Heart. 1. I will give them all the graces necessary in their state of life. "
            "2. I will establish peace in their homes. 3. I will comfort them in all their "
            "afflictions. 4. I will be their secure refuge during life, and above all in death. 5. I "
            "will bestow abundant blessings upon all their undertakings. 6. Sinners shall find in My "
            "Heart the source and the infinite ocean of mercy. 7. Tepid souls shall become fervent. "
            "8. Fervent souls shall quickly mount to high perfection. 9. I will bless every place in "
            "which an image of My Heart shall be exposed and honored. 10. I will give to priests the "
            "gift of touching the most hardened hearts. 11. Those who shall promote this devotion "
            "shall have their names written in My Heart, never to be effaced. 12. I promise you in "
            "the excessive mercy of My Heart that My all-powerful love will grant to all those who "
            "communicate on the First Friday in nine consecutive months the grace of final penitence; "
            "they shall not die in My disgrace nor without receiving their Sacraments. My divine "
            "Heart shall be their safe refuge in this last moment."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_the_sacred_heart_for_perseverance",
        title="Prayer to the Sacred Heart for Perseverance",
        text=(
            "O Sacred Heart of Jesus, living and life-giving fountain of eternal life, infinite "
            "treasure of the Divinity, and glowing furnace of love, You are my refuge and my "
            "sanctuary. O adorable and glorious Savior, consume my heart with that burning fire that "
            "ever inflames Your Heart. Pour down on my soul those graces which flow from Your love. "
            "Let my heart be so united with Yours that our wills may be one, and mine may in all "
            "things be conformed to Yours. May Your Will be the rule of both my desires and my "
            "actions. St. Alphonsus Liguori"
        ),
    ),
    Prayer(
        id="cbop_prayer_of_trust_in_the_sacred_heart",
        title="Prayer of Trust in the Sacred Heart",
        text=(
            "In all my temptations, I place my trust in You, O Sacred Heart of Jesus. In all my "
            "weaknesses, I place my trust in You, O Sacred Heart of Jesus. In all my difficulties, I "
            "place my trust in You, O Sacred Heart of Jesus. In all my trials, I place my trust in "
            "You, O Sacred Heart of Jesus. In all my sorrows, I place my trust in You, O Sacred Heart "
            "of Jesus. In all my work, I place my trust in You, O Sacred Heart of Jesus. In every "
            "failure, I place my trust in You, O Sacred Heart of Jesus. In every discouragement, I "
            "place my trust in You, O Sacred Heart of Jesus. In life and in death, I place my trust "
            "in You, O Sacred Heart of Jesus. In time and in eternity, I place my trust in You, O "
            "Sacred Heart of Jesus."
        ),
    ),
    Prayer(
        id="cbop_act_of_dedication_of_the_human_race_to_christ_the_king",
        title="Act of Dedication of the Human Race to Christ the King",
        text=(
            "Most sweet Jesus, Redeemer of the human race, look down upon us humbly prostrate before "
            "You. We are Yours, and Yours we wish to be; but to be more surely united with You, "
            "behold, each one of us freely consecrates himself today to Your Most Sacred Heart. Many "
            "indeed have never known You; many, too, despising Your precepts, have rejected You. Have "
            "mercy on them all, most merciful Jesus, and draw them to Your Sacred Heart. Be King, O "
            "Lord, not only of the faithful who have never forsaken You, but also of the prodigal "
            "children who have abandoned You; grant that they may quickly return to their Father's "
            "house, lest they die of wretchedness and hunger. Be King of those who are deceived by "
            "erroneous opinions, or whom discord keeps aloof, and call them back to the harbor of "
            "truth and the unity of faith, so that soon there may be but one flock and one Shepherd. "
            "Grant, O Lord, to Your Church assurance of freedom and immunity from harm; give "
            "tranquility of order to all nations; make the earth resound from pole to pole with one "
            "cry: Praise to the divine Heart that wrought our salvation; to it be glory and honor "
            "forever. Amen. A partial indulgence is granted to the faithful, who piously recite the "
            "above Act of Dedication of the Human Race to Christ the King. A plenary indulgence is "
            "granted, if it is recited publicly on the feast of Christ the King."
        ),
    ),
    Prayer(
        id="cbop_litany_of_the_most_sacred_heart_of_jesus",
        title="Litany of the Most Sacred Heart of Jesus",
        text=(
            "Lord, have mercy. Christ, have mercy. Lord, have mercy. Christ, hear us. Christ, "
            "graciously hear us. God, the Father of heaven, have mercy on us. God the Son, Redeemer "
            "of the world, God, the Holy Spirit, Holy Trinity, one God, Heart of Jesus, Son of the "
            "eternal Father, Heart of Jesus, formed by the Holy Spirit in the womb of the Virgin "
            "Mother, Heart of Jesus, substantially united to the Word of God, Heart of Jesus, of "
            "infinite majesty, Heart of Jesus, sacred temple of God, Heart of Jesus, tabernacle of "
            "the Most High, Heart of Jesus, house of God and gate of heaven, Heart of Jesus, burning "
            "furnace of love, Heart of Jesus, abode of justice and love, Heart of Jesus, full of "
            "goodness and love, Heart of Jesus, abyss of all virtues, Heart of Jesus, most worthy of "
            "all praise, Heart of Jesus, King and center of all hearts, Heart of Jesus, in Whom are "
            "all the treasures of wisdom and knowledge, Heart of Jesus, in Whom dwells the fullness "
            "of Divinity, Heart of Jesus, in Whom the Father was well pleased, Heart of Jesus, of "
            "Whose fullness we have all received, Heart of Jesus, desire of the everlasting hills, "
            "Heart of Jesus, patient and most merciful, Heart of Jesus, enriching all who invoke You, "
            "Heart of Jesus, fountain of life and holiness, Heart of Jesus, propitiation for our "
            "sins, Heart of Jesus, loaded down with opprobrium, Heart of Jesus, bruised for our "
            "offenses, Heart of Jesus, obedient to death, Heart of Jesus, pierced with a lance, Heart "
            "of Jesus, source of all consolation, Heart of Jesus, our life and resurrection, Heart of "
            "Jesus, our peace and reconciliation, Heart of Jesus, victim for our sins, Heart of "
            "Jesus, salvation of those who trust in You, Heart of Jesus, hope of those who die in "
            "You, Heart of Jesus, delight of all the Saints, Lamb of God, You take away the sins of "
            "the world; spare us, O Lord. Lamb of God, You take away the sins of the world; "
            "graciously hear us, O Lord. Lamb of God, You take away the sins of the world; have mercy "
            "on us. Jesus, meek and humble of heart. Make our hearts like to Yours. Let us pray. "
            "Almighty and eternal God, look upon the Heart of Your most beloved Son and upon the "
            "praises and satisfaction which He offers You in the name of sinners; and to those who "
            "implore Your mercy, in Your great goodness, grant forgiveness in the name of the same "
            "Jesus Christ, Your Son, Who lives and reigns with You forever and ever."
        ),
    ),
    Prayer(
        id="cbop_1_jesus_is_condemned_to_death",
        title="1. Jesus Is Condemned to Death",
        text=(
            "O Jesus, You desired to die for me that I may receive supernatural life, sanctifying "
            "grace, and become a child of God. How precious must be that life. Teach me to appreciate "
            "it more and help me never to lose it by sin."
        ),
    ),
    Prayer(
        id="cbop_2_jesus_bears_his_cross",
        title="2. Jesus Bears His Cross",
        text=(
            "O Jesus, You have chosen to die the disgraceful death on the Cross. You have paid a "
            "high price for my redemption and the life of grace that was bestowed upon me. May I love "
            "You always and bear my crosses for Your sake."
        ),
    ),
    Prayer(
        id="cbop_3_jesus_falls_the_first_time",
        title="3. Jesus Falls the First Time",
        text=(
            "O Jesus, Your painful fall under the Cross and Your quick rise teach me to repent and "
            "rise instantly should I ever be forgetful of Your love and commit a mortal sin. Make me "
            "strong enough to conquer my wicked passions."
        ),
    ),
    Prayer(
        id="cbop_4_jesus_meets_his_mother",
        title="4. Jesus Meets His Mother",
        text=(
            "O Jesus, Your afflicted Mother was resigned to Your Passion because she is my Mother "
            "also, and wants to see me live and die as a child of God. Grant me a tender love for You "
            "and Your holy Mother."
        ),
    ),
    Prayer(
        id="cbop_5_jesus_is_helped_by_simon",
        title="5. Jesus Is Helped by Simon",
        text=(
            "O Jesus, Simon first reluctantly helped You to carry the Cross. Make me better "
            "understand the value of my sufferings which should lead me closer to You, as Simon was "
            "united with You through the Cross."
        ),
    ),
    Prayer(
        id="cbop_6_jesus_and_veronica",
        title="6. Jesus and Veronica",
        text=(
            "O Jesus, how graciously did You reward that courageous woman. When I side with You "
            "against sin and temptation, You surely will increase the beauty of my soul and fill me "
            "with joy and peace. Jesus, give me courage."
        ),
    ),
    Prayer(
        id="cbop_7_jesus_falls_a_second_time",
        title="7. Jesus Falls a Second Time",
        text=(
            "O Jesus, despite my good resolutions I have sinned repeatedly. But Your sufferings "
            "assure me of forgiveness if only I return to You with a contrite heart. I repent for "
            "having offended You. Help me to avoid sin in the future."
        ),
    ),
    Prayer(
        id="cbop_8_jesus_speaks_to_the_women",
        title="8. Jesus Speaks to the Women",
        text=(
            "O Jesus, You told the women of Jerusalem to weep for their sins rather than for You. "
            "Make me weep for my sins which caused Your terrible sufferings and the loss of my "
            "friendship with You."
        ),
    ),
    Prayer(
        id="cbop_9_jesus_falls_a_third_time",
        title="9. Jesus Falls a Third Time",
        text=(
            "O Jesus, I see You bowed to the earth, enduring the pains of extreme exhaustion. Grant "
            "that I may never yield to despair in time of hardship and spiritual distress. Let me "
            "come to You for help and comfort."
        ),
    ),
    Prayer(
        id="cbop_10_jesus_is_stripped_of_his_garments",
        title="10. Jesus Is Stripped of His Garments",
        text=(
            "O Jesus, You permitted Yourself to be stripped of Your garments. Strip me of sin and "
            "clothe me with Your holiness. Grant that I may sacrifice all my unlawful attachments "
            "rather than imperil the divine life of my soul."
        ),
    ),
    Prayer(
        id="cbop_11_jesus_is_nailed_to_the_cross",
        title="11. Jesus Is Nailed to the Cross",
        text=(
            "O Jesus, how could I complain if nailed to God's commandments which are given for my "
            "salvation, when I see You nailed to the Cross! Strengthen my faith and increase my love "
            "for You. Help me keep the commandments."
        ),
    ),
    Prayer(
        id="cbop_12_jesus_dies_on_the_cross",
        title="12. Jesus Dies on the Cross",
        text=(
            "O Jesus, dying on the Cross, You preached love and forgiveness. May I be thankful that "
            "You have made me a child of God. Help me to forgive all who have injured me, so that I "
            "myself may obtain forgiveness."
        ),
    ),
    Prayer(
        id="cbop_13_jesus_is_taken_from_the_cross",
        title="13. Jesus Is Taken from the Cross",
        text=(
            "O Jesus, a sword of grief pierced Your Mother's heart when You were lying lifeless in "
            "her arms. Grant me through her intercession to lead the life of a loyal child of Mary, "
            "so that I may be received by her at my death."
        ),
    ),
    Prayer(
        id="cbop_14_jesus_is_placed_in_the_sepulcher",
        title="14. Jesus Is Placed in the Sepulcher",
        text=(
            "O Jesus, Your enemies triumphed when they sealed Your tomb. But Your eternal triumph "
            "began on Easter morning. Strengthen my good will to live for You until the divine life "
            "of my soul will be manifested in heaven."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_receive_the_holy_spirit",
        title="Prayer to Receive the Holy Spirit",
        text=(
            "O King of glory, send us the Promised of the Father, the Spirit of Truth. May the "
            "Counselor Who proceeds from You enlighten us and infuse all truth in us, as You have "
            "promised."
        ),
    ),
    Prayer(
        id="cbop_for_the_seven_gifts_of_the_spirit",
        title="For the Seven Gifts of the Spirit",
        text=(
            "O Lord Jesus, through You I humbly beg our merciful Father to send the Holy Spirit of "
            "grace, that He may bestow upon us His sevenfold gifts. May He send us the gift of wisdom "
            "which will make us relish the Tree of Life that is none other than Yourself; the gift of "
            "understanding which will enlighten us; the gift of counsel which will guide us in the "
            "way of righteousness; and the gift of fortitude which will give us the strength to "
            "vanquish the enemies of our sanctification and salvation. May He impart to us the gift "
            "of knowledge which will enable us to discern Your teaching and distinguish good from "
            "evil; the gift of piety which will make us enjoy true peace; and the gift of fear which "
            "will make us shun all iniquity and avoid all danger of offending Your Majesty. To the "
            "Father and to the Son and to the Holy Spirit be given all glory and thanksgiving "
            "forever. St. Bonaventure"
        ),
    ),
    Prayer(
        id="cbop_for_the_twelve_fruits_of_the_spirit",
        title="For the Twelve Fruits of the Spirit",
        text=(
            "Holy Spirit, eternal Love of the Father and the Son, kindly bestow on us the fruit of "
            "charity, that we may be united to You by divine love; the fruit of joy, that we may be "
            "filled with holy consolation; the fruit of peace, that we may enjoy tranquility of soul; "
            "and the fruit of patience, that we may endure humbly everything that may be opposed to "
            "our own desires. Divine Spirit, be pleased to infuse in us the fruit of benignity, that "
            "we may willingly relieve our neighbor's necessities; the fruit of goodness, that we may "
            "be benevolent toward all; the fruit of longanimity, that we may not be discouraged by "
            "delay but may persevere in prayer; and the fruit of mildness, that we may subdue every "
            "rising of ill temper, stifle every murmur, and repress the susceptibilities of our "
            "nature in all our dealings with our neighbor. Creator Spirit, graciously impart to us "
            "the fruit of fidelity, that we may rely with assured confidence on the word of God; the "
            "fruit of modesty, that we may act becomingly; and the fruits of continence and chastity, "
            "that we may keep our bodies in such holiness as befits Your temple, so that, having by "
            "Your assistance preserved our hearts pure on earth, we may merit in Jesus Christ, "
            "according to the words of the Gospel, to see God eternally in the glory of His Kingdom."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_union_with_the_holy_spirit",
        title="Prayer for Union with the Holy Spirit",
        text=(
            "O holy Spirit of Light and Love, to You I consecrate my heart, mind, and will for time "
            "and eternity. May I be ever docile to Your divine inspirations and to the teachings of "
            "the holy Catholic Church whose infallible guide You are. May my heart be ever inflamed "
            "with the love of God and love of neighbor. May my will be ever in harmony with Your "
            "divine Will. May my life faithfully imitate the life and virtues of our Lord and Savior "
            "Jesus Christ. To Him, with the Father, and You, divine Spirit, be honor and glory "
            "forever. St. Pius X"
        ),
    ),
    Prayer(
        id="cbop_archconfraternity_prayer_to_the_holy_spirit",
        title="Archconfraternity Prayer to the Holy Spirit",
        text=(
            "Holy Spirit, Lord of Light, from Your clear celestial height, Your pure beaming "
            "radiance give. Come, O Father of the Poor, come with treasures which endure, come, O "
            "Light of all that live. You of all Consolers best, and the soul's delightsome Guest, do "
            "refreshing Peace bestow. You in toil are Comfort sweet, pleasant Coolness in the heat, "
            "solace in the midst of woe. Light immortal, Light Divine, visit now this heart of mine, "
            "and my inmost being fill. If You take Your grace away, nothing pure in men will stay, "
            "all their good is turned to ill. Heal our wounds, our strength renew, on our dryness "
            "pour Your dew, wash the stains of guilt away. Bend the stubborn heart and will, melt the "
            "frozen, warm the chill, guide the steps that go astray. On all those who evermore You "
            "confess and You adore, in Your Sevenfold Gifts descend. Give them Comfort when they die. "
            "Give them Life with You on high, give them Joys which never end."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_the_indwelling_of_the_spirit",
        title="Prayer for the Indwelling of the Spirit",
        text=(
            "Holy Spirit, powerful Consoler, sacred Bond of the Father and the Son, Hope of the "
            "afflicted, descend into my heart and establish in it Your loving dominion. Enkindle in "
            "my tepid soul the fire of Your Love so that I may be wholly subject to You. We believe "
            "that when You dwell in us, You also prepare a dwelling for the Father and the Son. "
            "Deign, therefore, to come to me, Consoler of abandoned souls and Protector of the needy. "
            "Help the afflicted, strengthen the weak, and support the wavering. Come and purify me. "
            "Let no evil desire take possession of me. You love the humble and resist the proud. Come "
            "to me, glory of the living and hope of the dying. Lead me by Your grace that I may "
            "always be pleasing to You. St. Augustine of Hippo"
        ),
    ),
    Prayer(
        id="cbop_we_fly_to_your_patronage",
        title="We Fly to Your Patronage",
        text=(
            "We fly to your patronage, O holy Mother of God; despise not our petitions in our "
            "necessities, but deliver us always from all dangers, O glorious and blessed Virgin."
        ),
    ),
    Prayer(
        id="cbop_mary_mother_of_grace",
        title="Mary, Mother of Grace",
        text=(
            "Mary, Mother of grace, Mother of mercy, shield me from the enemy and receive me at the "
            "hour of my death."
        ),
    ),
    Prayer(
        id="cbop_holy_mary_help_the_helpless",
        title="Holy Mary, Help the Helpless",
        text=(
            "Holy Mary, help the helpless, strengthen the fearful, comfort the sorrowful, pray for "
            "the people, plead for the clergy, intercede for all women consecrated to God; may all "
            "who keep your sacred commemoration experience the might of your assistance. Partial "
            "indulgence."
        ),
    ),
    Prayer(
        id="cbop_remember_o_most_gracious_virgin_mary_the_memorare",
        title="Remember, O Most Gracious Virgin Mary (The \"Memorare\")",
        text=(
            "Remember, O most gracious Virgin Mary, that never was it known that anyone who fled to "
            "your protection, implored your help or sought your intercession was left unaided. "
            "Inspired with this confidence, I fly to you, O Virgin of virgins, my Mother; to you do I "
            "come, before you I stand, sinful and sorrowful. O Mother of the Word Incarnate, despise "
            "not my petitions, but in your mercy hear and answer me. Amen. Partial indulgence."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_our_lady_of_fatima",
        title="Prayer to Our Lady of Fatima",
        text=(
            "O most holy Virgin Mary, Queen of the most holy Rosary, you were pleased to appear to "
            "the children of Fatima and reveal a glorious message. We implore you, inspire in our "
            "hearts a fervent love for the recitation of the Rosary. By meditating on the mysteries "
            "of the redemption that are recalled therein may we obtain the graces and virtues that we "
            "ask, through the merits of Jesus Christ, our Lord and Redeemer."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_our_lady_of_good_counsel",
        title="Prayer to Our Lady of Good Counsel",
        text=(
            "Most glorious Virgin, you were chosen by the eternal Counsel to be the Mother of the "
            "eternal Word made flesh. You are the treasurer of divine graces and the advocate of "
            "sinners. I who am your most unworthy servant have recourse to you. Graciously be my "
            "guide and counselor in this valley of tears. Obtain for me, through the Precious Blood "
            "of your divine Son, the forgiveness of my sins, the salvation of my soul, and the means "
            "necessary to obtain it. In like manner, obtain for holy Church victory over her enemies "
            "and the spread of Jesus' kingdom over the whole earth."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_our_lady_of_guadalupe",
        title="Prayer to Our Lady of Guadalupe",
        text=(
            "Our Lady of Guadalupe, mystical rose, intercede for the Church, protect the Holy "
            "Father, help all who invoke you in their necessities. Since you are the ever Virgin Mary "
            "and Mother of the true God, obtain for us from your most holy Son the grace of a firm "
            "and a sure hope amid the bitterness of life, as well as an ardent love and the precious "
            "gift of final perseverance."
        ),
    ),
    Prayer(
        id="cbop_our_lady_help_of_christians",
        title="Our Lady, Help of Christians",
        text=(
            "Mary, powerful Virgin, you are the mighty and glorious protector of the Church. You are "
            "the marvelous help of Christians. You are awe-inspiring as an army in battle array. In "
            "the midst of our anguish, struggle, and distress, defend us from the power of the enemy, "
            "and at the hour of our death receive our soul in heaven."
        ),
    ),
    Prayer(
        id="cbop_our_lady_of_lourdes",
        title="Our Lady of Lourdes",
        text=(
            "O immaculate Virgin Mary, you are the refuge of sinners, the health of the sick, and "
            "the comfort of the afflicted. By your appearances at the Grotto of Lourdes you made it a "
            "privileged sanctuary where your favors are given to people streaming to it from the "
            "whole world. Over the years countless sufferers have obtained the cure of their "
            "infirmities—whether of soul, mind, or body. Therefore I come with limitless confidence "
            "to implore your motherly intercession."
        ),
    ),
    Prayer(
        id="cbop_how_to_say_the_rosary",
        title="How to Say the Rosary",
        text=(
            "1. Begin on the crucifix and say the Apostles' Creed. 2. On the 1st bead, say 1 Our "
            "Father. 3. On the next 3 beads, say Hail Mary. 4. Next say 1 Glory Be. Then announce and "
            "think of the first Mystery and what it means, and say 1 Our Father. 5. Say 10 Hail Marys "
            "and 1 Glory Be to the Father. 6. Announce the second Mystery and continue in the same "
            "way until each of the five Mysteries of the selected group or decades is said."
        ),
    ),
    Prayer(
        id="cbop_the_five_joyful_mysteries",
        title="The Five Joyful Mysteries",
        text=(
            "(Said on Mondays and Saturdays, and Sundays from Advent until Lent) The Joyful "
            "Mysteries direct our mind to the Son of God, Jesus Christ, our Lord and Savior, Who took "
            "human nature from a human mother, Mary. They also bring to our attention some of the "
            "extraordinary events that preceded, accompanied, and followed Christ's Birth."
        ),
    ),
    Prayer(
        id="cbop_1_the_annunciation",
        title="1. The Annunciation",
        text=(
            "Mary, you received with deep humility the news of the Angel Gabriel that you were to be "
            "the Mother of God's Son; obtain for me a similar humility."
        ),
    ),
    Prayer(
        id="cbop_2_the_visitation",
        title="2. The Visitation",
        text=(
            "Mary, you showed true charity in visiting Elizabeth and remaining with her for three "
            "months before the birth of John the Baptist; obtain for me the grace to love my "
            "neighbor."
        ),
    ),
    Prayer(
        id="cbop_3_the_birth_of_jesus",
        title="3. The Birth of Jesus",
        text=(
            "Jesus, You accepted poverty when You were placed in the manger although You were our "
            "God; grant that I may have the spirit of poverty."
        ),
    ),
    Prayer(
        id="cbop_4_the_presentation_in_the_temple",
        title="4. The Presentation in the Temple",
        text=(
            "Mary, you obeyed the law of God in presenting the Child Jesus in the Temple; obtain for "
            "me the virtue of obedience."
        ),
    ),
    Prayer(
        id="cbop_5_the_finding_in_the_temple",
        title="5. The Finding in the Temple",
        text=(
            "Mary, you were sad at the loss of Jesus and joyous on finding Him surrounded by "
            "teachers in the Temple; obtain for me the virtue of piety."
        ),
    ),
    Prayer(
        id="cbop_the_five_luminous_mysteries",
        title="The Five Luminous Mysteries",
        text=(
            "(Said on Thursdays [except during Lent]) The Luminous Mysteries recall to our mind "
            "important events of the Public Ministry of Christ through which He announces the coming "
            "of the Kingdom of God."
        ),
    ),
    Prayer(
        id="cbop_1_christ_s_baptism_in_the_jordan",
        title="1. Christ's Baptism in the Jordan",
        text=(
            "Jesus, at Your Baptism the Father called You His beloved Son and the Holy Spirit came "
            "upon You to invest You with Your mission; help me to keep my Baptismal Promises."
        ),
    ),
    Prayer(
        id="cbop_2_christ_s_self_manifestation_at_cana",
        title="2. Christ's Self-Manifestation at Cana",
        text=(
            "Mary, the first among believers in Christ, upon your intercession your Son changed "
            "water into wine and brought the disciples to faith; help me to do whatever Jesus says."
        ),
    ),
    Prayer(
        id="cbop_3_christ_s_proclamation_of_the_kingdom",
        title="3. Christ's Proclamation of the Kingdom",
        text=(
            "Jesus, You preached the Kingdom of God with its call to forgiveness, inaugurating the "
            "ministry of mercy; help me to seek forgiveness for my sins."
        ),
    ),
    Prayer(
        id="cbop_4_the_transfiguration_of_our_lord",
        title="4. The Transfiguration of Our Lord",
        text=(
            "Jesus, the glory of the Godhead shone forth from Your face as the Father commanded the "
            "Apostles to be transfigured by the Spirit; help me to be a new person in You."
        ),
    ),
    Prayer(
        id="cbop_5_christ_s_institution_of_the_eucharist",
        title="5. Christ's Institution of the Eucharist",
        text=(
            "Jesus, at the Last Supper, You offered Your Body and Blood as food under the signs of "
            "bread and wine and testified to Your love for humanity; help me to attain active "
            "participation at Mass."
        ),
    ),
    Prayer(
        id="cbop_the_five_sorrowful_mysteries",
        title="The Five Sorrowful Mysteries",
        text=(
            "(Said on Tuesdays and Fridays throughout the year, and daily from Ash Wednesday until "
            "Easter Sunday) The Sorrowful Mysteries recall to our mind the mysterious events "
            "surrounding Christ's sacrifice of His life so that sinful humanity might be reconciled "
            "with God."
        ),
    ),
    Prayer(
        id="cbop_1_the_agony_in_the_garden",
        title="1. The Agony in the Garden",
        text=(
            "Jesus, in the Garden of Gethsemane, You suffered a bitter agony because of our sins; "
            "grant me true contrition."
        ),
    ),
    Prayer(
        id="cbop_2_the_scourging_at_the_pillar",
        title="2. The Scourging at the Pillar",
        text=(
            "Jesus, You endured a cruel scourging and Your flesh was torn by heavy blows; help me to "
            "have the virtue of purity."
        ),
    ),
    Prayer(
        id="cbop_3_the_crowning_with_thorns",
        title="3. The Crowning with Thorns",
        text=(
            "Jesus, You patiently endured the pain from the crown of sharp thorns that was forced "
            "upon Your head; grant me the strength to have moral courage."
        ),
    ),
    Prayer(
        id="cbop_4_the_carrying_of_the_cross",
        title="4. The Carrying of the Cross",
        text=(
            "Jesus, You willingly carried your Cross for love of Your Father and all people; grant "
            "me the virtue of patience."
        ),
    ),
    Prayer(
        id="cbop_5_the_crucifixion",
        title="5. The Crucifixion",
        text=(
            "Jesus, for love of me You endured three hours of torture on the Cross and gave up Your "
            "Spirit; grant me the grace of final perseverance."
        ),
    ),
    Prayer(
        id="cbop_the_five_glorious_mysteries",
        title="The Five Glorious Mysteries",
        text=(
            "(Said on Wednesdays [except during Lent] and the Sundays from Easter until Advent) The "
            "Glorious Mysteries recall to our mind the ratification of Christ's sacrifice for the "
            "redemption of the world, and our sharing in the fruits of His sacrifice."
        ),
    ),
    Prayer(
        id="cbop_1_the_resurrection",
        title="1. The Resurrection",
        text=(
            "Jesus, You rose from the dead in triumph and remained for forty days with your "
            "disciples, instructing and encouraging them; increase my faith."
        ),
    ),
    Prayer(
        id="cbop_2_the_ascension",
        title="2. The Ascension",
        text=(
            "Jesus, in the presence of Mary and the disciples You ascended to heaven to sit at the "
            "Father's right hand; increase the virtue of hope in me."
        ),
    ),
    Prayer(
        id="cbop_3_the_descent_of_the_holy_spirit",
        title="3. The Descent of the Holy Spirit",
        text=(
            "Jesus, as You promised, You sent the Holy Spirit upon Mary and the disciples under the "
            "form of tongues of fire; increase my love for God."
        ),
    ),
    Prayer(
        id="cbop_4_the_assumption",
        title="4. The Assumption",
        text=(
            "Mary, by the power of God you were assumed into heaven and united with your Divine Son; "
            "help me to have true devotion to you."
        ),
    ),
    Prayer(
        id="cbop_5_the_crowning_of_the_blessed_virgin",
        title="5. The Crowning of the Blessed Virgin",
        text=(
            "Mary, you were crowned Queen of heaven by your Divine Son to the great joy of all the "
            "Saints; obtain eternal happiness for me."
        ),
    ),
    Prayer(
        id="cbop_prayer_after_the_rosary",
        title="Prayer After the Rosary",
        text=(
            "O God, Whose only-begotten Son, by His Life, Death, and Resurrection, has purchased for "
            "us the rewards of eternal life: grant, we beseech You, that, meditating upon these "
            "mysteries of the Most Holy Rosary of the Blessed Virgin Mary, we may imitate what they "
            "contain and obtain what they promise, through the same Christ our Lord."
        ),
    ),
    Prayer(
        id="cbop_litany_of_the_blessed_virgin_mary",
        title="Litany of the Blessed Virgin Mary",
        text=(
            "Lord, have mercy. Christ, have mercy. Lord, have mercy. Christ, hear us. Christ, "
            "graciously hear us. God, the Father of heaven, have mercy on us. God the Son, Redeemer "
            "of the world, have mercy on us. God the Holy Spirit, Holy Trinity, one God, Holy Mary, "
            "pray for us. Holy Mother of God, Holy Virgin of virgins, Mother of Christ, Mother of "
            "the Church, Mother of divine grace, Mother most pure, Mother most chaste, Mother "
            "inviolate, Mother undefiled, Mother most amiable, Mother most admirable, Mother of good "
            "counsel, Mother of our Creator, Mother of our Savior, Virgin most prudent, Virgin most "
            "venerable, Virgin most renowned, Virgin most powerful, Virgin most merciful, Virgin most "
            "faithful, Mirror of justice, Seat of wisdom, Cause of our joy, Spiritual vessel, Vessel "
            "of honor, Singular vessel of devotion, Mystical rose, Tower of David, Tower of ivory, "
            "House of gold, Ark of the covenant, Gate of heaven, Morning star, Health of the sick, "
            "Refuge of sinners, Comforter of the afflicted, Help of Christians, Queen of angels, "
            "Queen of patriarchs, Queen of prophets, Queen of apostles, Queen of martyrs, Queen of "
            "confessors, Queen of virgins, Queen of all saints, Queen conceived without original sin, "
            "Queen assumed into heaven, Queen of the most holy Rosary, Queen of families, Queen of "
            "peace, Lamb of God, You take away the sins of the world; spare us, O Lord! Lamb of God, "
            "You take away the sins of the world; graciously hear us, O Lord! Lamb of God, You take "
            "away the sins of the world; have mercy on us. Pray for us, O holy Mother of God. That we "
            "may be made worthy of the promises of Christ. Let us pray. Grant, we beg You, O Lord "
            "God, that we Your servants may enjoy lasting health of mind and body, and by the "
            "glorious intercession of the Blessed Mary, ever Virgin, be delivered from present sorrow "
            "and enter into the joy of eternal happiness. Through Christ our Lord. r Amen."
        ),
    ),
    Prayer(
        id="cbop_rosary_novena_prayer",
        title="Rosary Novena Prayer",
        text=(
            "Holy Virgin Mary, Mother of God and our Mother, accept this Holy Rosary which I offer "
            "you to show my love for you and my firm confidence in your powerful intercession. I "
            "offer it as an act of faith in the mysteries of the Incarnation and the Redemption, as "
            "an act of thanksgiving to God for all His love for me and all mankind, as an act of "
            "atonement for the sins of the world, especially my own, and as an act of petition to God "
            "through your intercession for all the needs of God's people on earth, but especially for "
            "this earnest request. (Mention your request.) I beg you, dear Mother of God, present my "
            "petition to Jesus, your Son. I know that you want me to seek God's will in my request. "
            "If what I ask for should not be God's will, pray that I may receive that which will be "
            "of greater benefit for my soul. I put all my confidence in you."
        ),
    ),
    Prayer(
        id="cbop_act_of_reparation",
        title="Act of Reparation",
        text=(
            "O most holy Virgin and our Mother, we listen with grief to the complaints of your "
            "Immaculate Heart surrounded with the thorns placed therein at every moment by the "
            "blasphemies and ingratitude of ungrateful humanity. We are moved by the ardent desire of "
            "loving you as our Mother and of promoting a true devotion to your Immaculate Heart. We "
            "therefore kneel before you to manifest the sorrow we feel for the grievances that people "
            "cause you, and to atone by our prayers and sacrifices for the offenses with which they "
            "return your love. Obtain for them and for us the pardon of so many sins. Hasten the "
            "conversion of sinners that they may love Jesus and cease to offend the Lord, already so "
            "much offended. Turn your eyes of mercy toward us, that we may love God with all our "
            "heart on earth and enjoy Him forever in heaven."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_st_joseph_2",
        title="Prayer to St. Joseph (II)",
        text=(
            "O glorious St. Joseph, you were chosen by God to be the foster father of Jesus, the "
            "most pure spouse of Mary, ever Virgin, and the head of the Holy Family. You have been "
            "chosen by Christ's Vicar as the heavenly Patron and Protector of the Church founded by "
            "Christ. Protect the Sovereign Pontiff and all bishops and priests united with him. Be "
            "the protector of all who labor for souls amid the trials and tribulations of this life; "
            "and grant that all peoples of the world may follow Christ and the Church He founded. "
            "Dear St. Joseph, accept the offering I make to you. Be my father, protector, and guide "
            "in the way of salvation. Obtain for me purity of heart and a love for the spiritual "
            "life. After your example, let all my actions be directed to the greater glory of God, in "
            "union with the Divine Heart of Jesus, the Immaculate Heart of Mary, and your own "
            "paternal heart. Finally, pray for me that I may share in the peace and joy of your holy "
            "death."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_st_joseph_for_a_happy_death",
        title="Prayer to St. Joseph for a Happy Death",
        text=(
            "O blessed Joseph, you gave forth your last breath in the loving embrace of Jesus and "
            "Mary. When the seal of death shall close my life, come with Jesus and Mary to aid me. "
            "Obtain for me this solace for that hour—to die with their holy arms around me. Jesus, "
            "Mary, Joseph, I commend my soul, living and dying, into your sacred arms."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_st_michael_the_archangel_patron_of_the_sick",
        title="Prayer to St. Michael the Archangel Patron of the Sick",
        text=(
            "St. Michael the Archangel, defend us in the day of battle; be our safeguard against the "
            "wiles and wickedness of the devil. May God rebuke him, we humbly pray, and do thou, O "
            "prince of the heavenly host, by the power of God cast into hell Satan and all the other "
            "evil spirits, who prowl through the world, seeking the ruin of souls."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_one_s_guardian_angel_daily_protector_throughout_life",
        title="Prayer to One's Guardian Angel Daily Protector Throughout Life",
        text=(
            "Dear Angel, in His goodness God gave you to me to guide, protect, and enlighten me, and "
            "to bring me back to the right way when I go astray. Encourage me when I am disheartened, "
            "and instruct me when I err in my judgment. Help me to become more Christlike, and so "
            "some day to be accepted into the company of Angels and Saints in heaven."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_st_anne_patroness_of_homemakers",
        title="Prayer to St. Anne Patroness of Homemakers",
        text=(
            "Dear Saint, we know nothing about you except your name. But you gave us the Mother of "
            "God who called herself handmaid of the Lord. In your home you raised the Queen of Heaven "
            "and are rightly the model of homemakers. In your womb came to dwell the new Eve uniquely "
            "conceived without sin. Intercede for us that we too may remain free from sin."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_st_monica_patroness_of_mothers",
        title="Prayer to St. Monica Patroness of Mothers",
        text=(
            "Exemplary Mother of the great Augustine, you perseveringly pursued your wayward son "
            "with love and affection and pardon and counsel and powerful cries to heaven. Intercede "
            "for all mothers in our day so that they may learn to draw their children to God. Teach "
            "them how to remain close to their children, even the prodigal sons and daughters who "
            "have sadly gone astray."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_st_theresa_of_the_child_jesus_patroness_of_missionaries",
        title="Prayer to St. Theresa of the Child Jesus Patroness of Missionaries",
        text=(
            "Dear Little Flower of Lisieux, how wonderful was the short life you led. Though "
            "cloistered, you went far and wide through fervent prayers and great sufferings. You "
            "obtained from God untold helps and graces for his evangelists. Help all missionaries in "
            "their work and teach all of us to spread Christianity in our own neighborhoods and "
            "family circles."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_st_christopher_patron_of_motorists",
        title="Prayer to St. Christopher Patron of Motorists",
        text=(
            "Dear Saint, you have inherited a beautiful name — Christopher — as a result of a "
            "wonderful legend that while carrying people across a raging stream you also carried the "
            "Child Jesus. Teach us to be true Christ-bearers to those who do not know Him. Protect "
            "all drivers who often transport those who bear Christ within them."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_st_francis_of_assisi_patron_of_catholic_action",
        title="Prayer to St. Francis of Assisi Patron of Catholic Action",
        text=(
            "Dear Saint, once worldly and vain, you became humble and poor for the sake of Jesus and "
            "had an extraordinary love for the Crucified, which showed itself in your body by the "
            "imprints of Christ's Sacred Wounds. In our selfish and sensual age, how greatly we need "
            "your secret that draws countless men and women to imitate you. Teach us also great love "
            "for the poor and unswerving loyalty to the Vicar of Christ."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_st_jude_patron_of_desperate_causes",
        title="Prayer to St. Jude Patron of Desperate Causes",
        text=(
            "St. Jude, apostle of Christ, the Church honors and prays to you universally as the "
            "patron of hopeless and difficult cases. Pray for us in our needs. Make use, we implore "
            "you, of this powerful privilege given to you to bring visible and speedy help where help "
            "is needed. Pray that we humbly accept the trials and disappointments and mistakes which "
            "are a part of our human nature. Let us see the reflection of the sufferings of Christ in "
            "our daily trials and tribulations. Let us see in a spirit of great faith and hope the "
            "part we even now share in the joy of Christ's resurrection, and which we long to share "
            "fully in heaven. Intercede that we may again experience this joy in answer to our "
            "present needs if it is God's desire for us. (Here make your request.) We know our "
            "prayers will be heard through your intercession."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_st_anthony_patron_of_motorists",
        title="Prayer to St. Anthony Patron of Motorists",
        text=(
            "O holy St. Anthony, gentlest of Saints, your love for God and charity for His creatures "
            "made you worthy even on earth to possess miraculous powers. Miracles waited on your word "
            "which you were ever ready to speak for those in trouble or anxiety. Encouraged by this "
            "thought, I implore you to obtain for me my request (here mention your intention). The "
            "answer to my prayer may require a miracle; even so, you are the Saint of miracles. O "
            "gentle and loving St. Anthony, whose heart is ever full of human sympathy, whisper my "
            "petition into the ears of the sweet Infant Jesus, Who loved to be enfolded in your arms, "
            "and the gratitude of my heart will be ever yours."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_st_rita_patroness_of_impossible_cases",
        title="Prayer to St. Rita Patroness of Impossible Cases",
        text=(
            "Holy Patroness of those in need, St. Rita, your pleadings before your divine Lord are "
            "irresistible. For your lavishness in granting favors you have been called the \"Advocate "
            "of the Hopeless\" and even of the \"Impossible.\" You are so humble, so mortified, so "
            "patient, and so compassionate in love for your crucified Jesus that you can obtain from "
            "Him anything you ask if it is His Holy Will. Therefore, all confidently have recourse to "
            "you in the hope of comfort or relief. Be propitious toward your suppliants and show your "
            "power with God in their behalf. Be generous with your favors now as you have been in so "
            "many wonderful cases for the greater glory of God, the spread of your devotion, and the "
            "consolation of those who trust in you. We promise, if our petition is granted, to "
            "glorify you by making known your favor, and to bless you and sing your praises. Relying "
            "then on your merits and power before the Sacred Heart of Jesus, we ask of you (here "
            "mention your request)."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_st_francis_xavier_patron_of_foreign_missions",
        title="Prayer to St. Francis Xavier Patron of Foreign Missions",
        text=(
            "O very dear St. Francis Xavier, full of divine charity, with you I reverently adore the "
            "divine Majesty. Since I greatly rejoice in the singular gifts of grace that the Lord "
            "conferred on you in this life, and of glory after death, I return most heartfelt thanks "
            "to him, and I beg you to obtain for me, by your powerful intercession, above all the "
            "grace to love God well. I also ask you to gain for me (here insert your petition). But "
            "if that which I suppliantly ask of you is not for the greater good of my soul, I beg you "
            "to obtain for me whatever will better promote both these ends."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_st_lucy_patroness_of_the_blind",
        title="Prayer to St. Lucy Patroness of the Blind",
        text=(
            "Dear holy Virgin and Martyr, whom the Church recalls in Eucharistic Prayer I, you "
            "valiantly rejected great promises and resisted several threats in remaining faithful to "
            "your beloved Lord. For centuries Christians have invoked you particularly when suffering "
            "from eye-trouble. So now we implore your assistance on behalf of N…. We also ask you to "
            "teach us to imitate you and to avoid spiritual blindness of any kind."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_st_vincent_de_paul_patron_of_charitable_societies",
        title="Prayer to St. Vincent De Paul Patron of Charitable Societies",
        text=(
            "O God, You gave St. Vincent de Paul apostolic virtues for the salvation of the poor and "
            "the formation of the clergy. Grant that, endowed with the same spirit, we may love what "
            "he loved and act according to his teaching."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_st_patrick_patron_of_ireland",
        title="Prayer to St. Patrick Patron of Ireland",
        text=(
            "Dear St. Patrick, in your humility you called yourself a sinner, but you became a most "
            "successful missionary and prompted countless pagans to follow the Savior. Many of their "
            "descendants in turn spread the Good News in numerous foreign lands. Through your "
            "powerful intercession with God, obtain for us the missionaries we need to continue the "
            "work you began."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_cities",
        title="Prayer for Cities",
        text=(
            "Cities are for needs and wants, divine Father, that cannot be met in isolation. Have we "
            "expected from them too much and put in too little? Spur us to renew our cities as You "
            "renew the earth in spring, that families may have decent living space, that the poor may "
            "have hope fulfilled, that the sick and aged may be treated as persons. May our cities be "
            "filled with love, truly homes and not merely structures. Amen. The Christophers"
        ),
    ),
    Prayer(
        id="cbop_prayer_for_all_people",
        title="Prayer for All People",
        text=(
            "O Lord, we bring before You the distress and dangers of peoples and nations, the pleas "
            "of the imprisoned and the captive, the sorrows of the grief-stricken, the needs of the "
            "refugees, the impotence of the weak, the weariness of the despondent, and the weaknesses "
            "of the aging. O Lord, stay close to all of them."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_christ_s_mercy",
        title="Prayer for Christ's Mercy",
        text=(
            "O Lord, show Your mercy to me, and gladden my heart. I am like the man on the way to "
            "Jericho who was overtaken by robbers, wounded, and left half-dead: O Good Samaritan, "
            "come to my aid. I am like the sheep that went astray: O Good Shepherd, seek me out and "
            "bring me home in accord with Your will. Let me dwell in Your house all the days of my "
            "life and praise You for ever and ever with those who are there."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_friends",
        title="Prayer for Friends",
        text=(
            "Lord Jesus Christ, while on earth You had close and devoted friends, such as John, "
            "Lazarus, Martha, and Mary. You showed in this way that friendship is one of life's "
            "greatest blessings. Thank You for the friends that You have given me to love me in spite "
            "of my failures and weaknesses, and to enrich my life after Your example. Let me ever "
            "behave toward them as You behaved toward Your friends. Bind us close together in You and "
            "enable us to help one another on our earthly journey."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_those_who_study_or_teach_christian_doctrine",
        title="Prayer for Those Who Study or Teach Christian Doctrine",
        text=(
            "Lord Jesus Christ, by Your Holy Spirit You give to some the word of wisdom, to others "
            "the word of knowledge, and to still others the word of faith. Grant us a knowledge of "
            "the Father and of Yourself. Help us to cling steadfastly to the Catholic faith. In our "
            "studies and in our teaching make us seek only the extension of Your kingdom and Your "
            "holy Church both in ourselves and in others."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_priestly_or_religious_vocations",
        title="Prayer for Priestly or Religious Vocations",
        text=(
            "O Lord, send workers for Your harvest, so that the precepts of Your only-begotten Son "
            "may always be obeyed and His sacrifice be everywhere renewed. Look with favor upon Your "
            "family, and ever increase its numbers. Enable it to lead its sons and daughters to the "
            "holiness to which they are called and to work for the salvation of others. Through "
            "Christ our Lord."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_all_church_leaders",
        title="Prayer for All Church Leaders",
        text=(
            "Lord Jesus Christ, watch over those who are leaders in Your Church. Keep them faithful "
            "to their vocation and to the proclamation of Your message. Strengthen them with the "
            "gifts of the Spirit and help them to serve Your people, especially the poor and lowly. "
            "Give them a vivid sense of Your presence in the world and a knowledge of how to show it "
            "to others."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_priests",
        title="Prayer for Priests",
        text=(
            "Almighty Father, grant to these servants of Yours the dignity of the priesthood. Renew "
            "within them the Spirit of holiness. As co-workers with the order of bishops may they be "
            "faithful to the ministry that they receive from You, Lord God, and be to others a model "
            "of right conduct. May they be faithful in spreading the good news, so that the words of "
            "the Gospel may reach the ends of the earth, and the family of nations, made one in "
            "Christ, may become God's one, holy people."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_missionaries",
        title="Prayer for Missionaries",
        text=(
            "Lord Jesus Christ, watch over Your missionaries—priests, religious, and lay people—who "
            "leave everything to give testimony to Your Word and Your love. In difficult moments "
            "sustain their energies, comfort their hearts, and crown their work with spiritual "
            "achievements. Let the adorable image of You crucified on the Cross, which accompanies "
            "them throughout life, speak to them of heroism, generosity, love, and peace."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_the_unity_of_the_church",
        title="Prayer for the Unity of the Church",
        text=(
            "Heavenly Father, Your blessed Son asked that His Church be one as You and He are one, "
            "but Christians have not been united as He prayed. We have isolated ourselves from each "
            "other and failed to listen to each other. We have misunderstood and ridiculed and even "
            "gone so far as to attack each other. In so doing we have offended against You, against "
            "all our brothers and sisters in the Church, and against all who have not believed in You "
            "because of our scandalous disunity. Forgive us, Father, and make us fully one. Blot out "
            "our sins, renew our minds, enkindle our hearts, and guide us by Your Holy Spirit into "
            "that oneness which is Your will."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_achieve_inner_peace",
        title="Prayer to Achieve Inner Peace",
        text=(
            "Slow me down, Lord. Ease the pounding of my heart by the quieting of my mind. Steady my "
            "hurried pace with a vision of the eternal reach of time. Give me, amid the confusion of "
            "the day, the calmness of the everlasting hills. Break the tensions of my nerves and "
            "muscles with the soothing music of the singing streams that live in memory. Help me to "
            "know the magical, restoring power of sleep. Teach me the art of taking minute "
            "vacations—of slowing down to look at a flower, to chat with a friend, to pat a dog, to "
            "read a few lines from a good book. Slow me down, Lord."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_acceptance_of_god_s_holy_will",
        title="Prayer for Acceptance of God's Holy Will",
        text=(
            "Dear God, I know that You love me because You died on the Cross for me. I know that You "
            "want nothing for me but the best in the light of eternity. So I trust in Your infinite "
            "wisdom and goodness and ask You to grant my request if it is according to Your holy "
            "will. I accept whatever You decide. I leave everything up to Your divine goodness and "
            "loving care. You are my God."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_the_family",
        title="Prayer for the Family",
        text=(
            "Lord God, from You every family in heaven and on earth takes its name. Father, you are "
            "Love and Life. Through Your Son, Jesus Christ, born of woman, and through the Holy "
            "Spirit, fountain of divine charity, grant that every family on earth may become for each "
            "successive generation a true shrine of life and love. Grant that Your grace may guide "
            "the thoughts and actions of husbands and wives for the good of their families and of all "
            "the families in the world. Grant that the young may find in the family solid support for "
            "their human dignity and for their growth in truth and love. Grant that love, "
            "strengthened by the Sacrament of marriage, may prove mightier than all the weaknesses "
            "and trials through which our families sometimes pass. Through the intercession of the "
            "Holy Family of Nazareth, grant that the Church may fruitfully carry out her worldwide "
            "mission in and through the family. Through Christ our Lord, Who is the Way, the Truth "
            "and the Life for ever and ever. Amen. Pope John Paul II"
        ),
    ),
    Prayer(
        id="cbop_prayer_of_the_aging",
        title="Prayer of the Aging",
        text=(
            "May Christ keep me ever young \"to the greater glory of God.\" For old age comes from "
            "Him, old age leads to Him, and old age will touch me only insofar as He wills. To be "
            "\"young\" means to be hopeful, energetic, and smiling. May I accept death in whatever "
            "guise it may come to me in Christ, that is, within the process of the development of "
            "life. A smile (inward and outward) means facing with mildness and gentleness whatever "
            "befalls me. Jesus, grant me to serve You, to proclaim You, to glorify You, and to "
            "manifest You, to the very end through all the time that remains to me of life, and above "
            "all through my death. Lord Jesus, I commit to Your care my last years, and my death; do "
            "not let them impair or spoil the work I have so dreamed of achieving for You."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_international_organizations",
        title="Prayer for International Organizations",
        text=(
            "Heavenly Father, You created this vast and wonderful universe, redeemed it in the Blood "
            "of Your Son, and now guide it by Your Holy Spirit. It is Your will that we live as "
            "brothers and sisters, building up the world by the marvelous powers that You have "
            "graciously given us. Look graciously on the representatives of the nations who are "
            "gathered together today for the good of all. Enlighten them to put forth wise proposals "
            "in accord with Your will. Teach them to deliberate with honesty and with genuine respect "
            "for one another. Help them to make just decisions that will redound to the peace and "
            "welfare of all nations."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_the_hungry",
        title="Prayer for the Hungry",
        text=(
            "Lord Jesus Christ, You urged us to give You food in Your hunger which is visible to us "
            "in the starving faces of other human beings. Let me realize that there are millions of "
            "persons—children of the same God and our brothers and sisters—who are dying of hunger "
            "although they do not deserve to do so. Do not allow me to remain indifferent to their "
            "crying need, or to soothe my conscience with the thought that I cannot do anything about "
            "this evil. Help me to do something—no matter how small—to alleviate their heart-rending "
            "want. Also let me pray regularly that these poor starving people will be rewarded for "
            "this terrible suffering they are enduring, and be relieved of it as soon as possible."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_the_grace_to_help_others",
        title="Prayer for the Grace to Help Others",
        text=(
            "Lord, make me an instrument of Your peace. Where there is hatred, let me sow love. "
            "Where there is injury, let me sow pardon. Where there is friction, let me sow union. "
            "Where there is error, let me sow truth. Where there is doubt, let me sow faith. Where "
            "there is despair, let me sow hope. Where there is darkness, let me sow light. Where "
            "there is sadness, let me sow joy. O Divine Master, grant that I may not so much seek to "
            "be consoled as to console, to be understood as to understand, to be loved as to love. "
            "For it is in giving that we receive. It is in pardoning that we are pardoned. It is in "
            "dying that we are born to eternal life. St. Francis of Assisi"
        ),
    ),
    Prayer(
        id="cbop_prayer_before_departing_on_a_trip",
        title="Prayer Before Departing on a Trip",
        text=(
            "O God, You called Abraham Your servant out of Ur and kept him safe and sound in all his "
            "wandering. We humbly ask You to protect us Your servants. Be for us a support when "
            "setting out, friendship along the way, a little shade from the sun, a safeguard in time "
            "of danger, and a haven in shipwreck. Bear us up in fatigue, and defend us under attack. "
            "Under Your protection, let us fulfill the purpose for our trip and return safe and sound "
            "to our home."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_work_for_the_things_we_pray_for",
        title="Prayer to Work for the Things We Pray For",
        text=(
            "O Lord, give us a mind that is humble, quiet, peaceable, patient, and charitable, and "
            "the inspiration of Your Holy Spirit in all our thoughts, words, and deeds. O Lord, give "
            "us a lively faith, a firm hope, a fervent charity, and a love of You. Take from us all "
            "lukewarmness in meditation and dullness in prayer. Give us fervor and delight in "
            "thinking of You, Your grace, and Your tender compassion toward us. Give us, good Lord, "
            "the grace to work for the things we pray for."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_health_wisdom_and_a_sense_of_humor",
        title="Prayer for Health, Wisdom, and a Sense of Humor",
        text=(
            "O Lord, give me a good digestion as well as something to digest. Give me health of body "
            "as well as the sense to keep it healthy. Give me a holy soul, O Lord, which keeps its "
            "eyes on beauty and purity, so that it will not be daunted on seeing sin. Give me a soul "
            "that knows nothing of boredom, groans, and sighs. Never let me be overly concerned for "
            "this inconstant thing that I call me. Lord, give me a sense of humor, so that I may take "
            "some happiness from this life, and share it with others."
        ),
    ),
    Prayer(
        id="cbop_prayer_of_self_offering_to_god",
        title="Prayer of Self-Offering to God",
        text=(
            "Take, O Lord, and receive my entire liberty, my memory, my understanding, and my whole "
            "will. All that I am and all that I possess You have given me. I surrender it all to You "
            "to be disposed of according to Your will. Give me only Your love and Your grace; with "
            "these I will be rich enough and will desire nothing more."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_fortitude",
        title="Prayer for Fortitude",
        text=(
            "Dear Jesus, lay your Wounded Hand Upon my weary head, And teach me to have courage In "
            "the paths that I must tread. Bless me, and bless those whom I love, And give us grace to "
            "see These crosses bravely borne by us Will keep us close to Thee. And if at times a "
            "shadow falls In unexpected ways, Put Your gentle Hand in mine And guide me through the "
            "days. So bless my people, one and all, With Thy protecting grace, And impart to them Thy "
            "Wisdom Ere they meet Thee face to face."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_employment",
        title="Prayer for Employment",
        text=(
            "Blessed Anthony, our intercessor in times of need, you gave yourself as a tireless "
            "worker in the vineyard of the Lord. By our labor we produce the things needed for human "
            "life. So our work is honorable and holy and makes perfect the work of God's creation. "
            "Pray that I may find work which enhances my human dignity, draws me closer to God, and "
            "makes my life, as was yours, a real service to my fellow men. Provide for me while I am "
            "in this trial of unemployment. I need your help, blessed friend. Come to my aid."
        ),
    ),
    Prayer(
        id="cbop_prayer_of_the_expectant_mother_to_saint_gerard_majella",
        title="Prayer of the Expectant Mother to Saint Gerard Majella",
        text=(
            "O great Saint Gerard, beloved servant of Jesus Christ, perfect imitator of thy meek and "
            "humble Savior, and devoted Child of the Mother of God: enkindle within my heart one "
            "spark of that heavenly fire of charity which glowed in thine and made thee a seraph of "
            "love. O glorious Saint Gerard, because, when falsely accused of crime, thou didst bear, "
            "like thy Divine Master, without murmur or complaint, the calumnies of wicked men, thou "
            "hast been raised up by God as the Patron and Protector of expectant mothers. Preserve me "
            "from danger and from the excessive pains accompanying childbirth, and shield the child "
            "which I now carry, that it may see the light of day and receive the lustral waters of "
            "baptism, through Jesus Christ our Lord. Amen. (Nine Hail Marys) Rev. Joseph A. Chapoton, "
            "C.SS.R."
        ),
    ),
    Prayer(
        id="cbop_prayer_of_complete_trust_in_god",
        title="Prayer of Complete Trust in God",
        text=(
            "O Lord, help me to realize that nothing will happen to me today that You and I cannot "
            "work out together."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_the_acceptance_of_god_s_will",
        title="Prayer for the Acceptance of God's Will",
        text=(
            "O Lord, I do not know what to ask You. You alone know my real needs, and You love me "
            "more than I even know how to love. Enable me to discern my true needs which are hidden "
            "from me. I ask for neither a cross nor a consolation but simply wait in patience for "
            "You. My heart is open to You. For Your great mercy's sake, come to me and help me. Put "
            "Your mark on me and heal me, cast me down and raise me up. I silently adore Your holy "
            "will and Your inscrutable ways. I offer myself in sacrifice to You and put all my trust "
            "in You. I desire only to do Your will. Teach me how to pray."
        ),
    ),
    Prayer(
        id="cbop_prayer_of_resignation_in_suffering",
        title="Prayer of Resignation in Suffering",
        text=(
            "Merciful Lord of life, I lift up my heart to You in my suffering and ask for Your "
            "comforting help. I know that You would withhold the thorns of this life if I could "
            "attain eternal life without them. So I throw myself on Your mercy, resigning myself to "
            "this suffering. Grant me the grace to bear it and to offer it in union with Your "
            "sufferings. No matter what suffering may come my way, let me trust in You."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_the_restoration_of_health",
        title="Prayer for the Restoration of Health",
        text=(
            "O Sacred Heart of Jesus, I come to ask You for the gift of restored health that I may "
            "serve You more faithfully and love You more sincerely. I want to be well if it is Your "
            "will and redounds to Your glory. If on the other hand it is Your will that my sickness "
            "continue, I want to bear it with patience. If in Your divine wisdom I am to be restored "
            "to health and strength, I will strive to show my gratitude by a constant and faithful "
            "service rendered to You, my loving Savior and Redeemer, and my God."
        ),
    ),
    Prayer(
        id="cbop_prayer_to_god_the_source_of_health",
        title="Prayer to God, the Source of Health",
        text=(
            "God our Father, source of all health, be near those who suffer in the time of weakness "
            "and pain; relieve them of their burden and heal them, if it be Your will. Give peaceful "
            "sleep to those who need rest for soul and body, and be with them in their hours of "
            "silence. Bless those who know not what another day will bring. Make them ready for "
            "whatever it may be. Whether they must stand, or sit or be confined, grant them a strong "
            "spirit. Inspire with Your love those who bring healing and care to the suffering. May "
            "they bestow Your gifts of health and strength wherever they go. Grant this prayer, "
            "through Christ our Lord."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_the_dead",
        title="Prayer for the Dead",
        text=(
            "God our Father, Your power brings us to birth, Your providence guides our lives, and by "
            "Your command we return to dust. I pray for the dead, especially for N. May those who "
            "have been dear to me in life find a place with You in heaven. Lord, those who die still "
            "live in Your presence; their lives change but do not end. I pray in hope for my family, "
            "relatives and friends, and for all the dead known to You alone. In company with Christ "
            "Who died and now lives may they rejoice in Your kingdom where all our tears are wiped "
            "away. Unite us together again as one family, to sing Your praise forever and ever."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_departed_relatives_friends_and_benefactors",
        title="Prayer for Departed Relatives, Friends and Benefactors",
        text=(
            "Heavenly Father, accept my prayer for all those in purgatory for whom I should pray "
            "because of ties of family, gratitude, justice, or charity. Have mercy on my relatives, "
            "friends, and benefactors as well as those who hold positions of authority, both civil "
            "and religious. Admit them all to Your eternal happiness in heaven. Eternal rest grant to "
            "them, O Lord. And let perpetual light shine upon them. May they rest in peace."
        ),
    ),
    Prayer(
        id="cbop_prayer_for_all_the_faithful_departed",
        title="Prayer for All the Faithful Departed",
        text=(
            "Heavenly Father, I believe that in Your wisdom and justice You willed to purify all "
            "persons who die without having attained the state that they need for all eternity, all "
            "who have still to expiate completely the sins committed on earth. I also believe that "
            "You have mercifully arranged that this process of purification can be aided by the "
            "prayers of the living, especially the Eucharist. Help me to pray for my brothers and "
            "sisters who have departed from this world. May their time of purification be short and "
            "they be quickly guided into that holy light promised by our Lord to Abraham and his "
            "descendants. I offer You sacrifices and prayers of praise. Accept them for all the souls "
            "of the faithful departed and admit them all to heavenly joy."
        ),
    ),
]


def get_prayer(prayer_id: str) -> Prayer:
    for prayer in PRAYERS:
        if prayer.id == prayer_id:
            return prayer
    raise KeyError(prayer_id)
