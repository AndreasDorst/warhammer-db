from models import Base
from scripts import engine, add_hero, add_story, add_moto, add_battle


def create_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def fill_database():
    add_hero(side="Forces of Chaos", name="Ahzek Ahriman", power=5)
    add_hero(side="Forces of Chaos", name="Lorgar Aurelian", power=5)
    add_hero(side="Forces of Chaos", name="Magnus the Red", power=7)
    add_hero(side="Imperium of Man", name="Roboute Guilliman", power=8)
    add_hero(side="Imperium of Man", name="Marneus Calgar", power=6)
    add_hero(side="Imperium of Man", name="Leman Russ", power=7)

    add_moto(hero_id=1, moto="I have forgotten nothing, and my wisdom has expanded far beyond mere mortal frailties.")
    add_moto(hero_id=1, moto="And what are the achievements of your fragile Imperium?")
    add_moto(hero_id=2, moto="All I ever wanted was the truth.")
    add_moto(hero_id=2, moto="Reaving half the galaxy clean of human life in this bitter crusade.")
    add_moto(hero_id=3, moto="Without the light of Chaos, the universe would stagnate and collapse.")
    add_moto(hero_id=3, moto="Only through the struggle, can any advancement occur.")
    add_moto(hero_id=4, moto="Better that we had all burned in the fires of Horus' ambition than live to see this.")
    add_moto(hero_id=4, moto="I gave everything I had to you, to them.")
    add_moto(hero_id=5, moto="We are the Ultramarines, the Sons of Guilliman.")
    add_moto(hero_id=5, moto="Nothing shall stay our wrath.")
    add_moto(hero_id=6, moto="Here I am and Here I shall Die.")
    add_moto(hero_id=6, moto="At the end I will be there. For the final battle. For the Wolftime.")
    
    add_story(hero_id=1, story="Ahriman, whose full name is Ahzek Ahriman, is a Chaos Space Marine and the most powerful Chaos Sorcerer of the Thousand Sons Traitor Legion after their Daemon Primarch Magnus the Red himself. Ahzek Ahriman was once the Chief Librarian and first captain of the ancient Thousand Sons Legion.")
    add_story(hero_id=2, story="Lorgar, also once called Lorgar Aurelian and the Urizen (Colchisian for 'wisest of the wise') before the Horus Heresy, is a Daemon Prince of Chaos Undivided and the Primarch of the Word Bearers Traitor Legion.")
    add_story(hero_id=3, story="Magnus the Red, the Primarch of the Thousand Sons Traitor Legion, is one of the few surviving primarchs and is currently an extremely powerful Daemon Prince of the Chaos God Tzeentch. He was also known during the early years of the Imperium as the 'Crimson King' and the 'Red Cyclops.'")
    add_story(hero_id=4, story="Roboute Guilliman (pronounced Ruh-BOOT-ay GIL-li-man), sometimes referred to as the 'Avenging Son,' 'The Victorious,' 'The Master of Ultramar' and 'The Blade of Unity,' is the primarch of the Ultramarines Space Marine Legion and its myriad subsequent Successor Chapters. He is the current lord commander of the Imperium and the ruling Imperial Regent.")
    add_story(hero_id=5, story="Marneus Augustus Calgar (pronounced Mar-NAY-us Cal-gar) is the current Chapter Master of the Ultramarines Space Marines Chapter, Lord Defender of Greater Ultramar and the Lord of Macragge, capital world of the Realm of Ultramar in the Eastern Fringes of the galaxy. He is believed to be the first known Firstborn Space Marine to undergo the arcane process to be transformed into an even more potent Primaris Space Marine.")
    add_story(hero_id=6, story="Leman Russ, also known as the 'Wolf King' and the 'Great Wolf' during his lifetime, is the currently missing Primarch of the Space Wolves Chapter of Space Marines. He led the Space Wolves Space Marine Legion during the Great Crusade and the Horus Heresy and is famed in Imperial history for his hatred of psychic powers and sorcery, whose use in battle he viewed as dishonourable and unworthy of true warriors.")
    
    for battle in range(10):
        add_battle()
    

if __name__ == '__main__':
    create_database()
    fill_database()
