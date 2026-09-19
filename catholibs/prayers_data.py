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
]


def get_prayer(prayer_id: str) -> Prayer:
    for prayer in PRAYERS:
        if prayer.id == prayer_id:
            return prayer
    raise KeyError(prayer_id)
