
# Skyrama Private Server

Skyrama Private Server is an attempt to create a custom server for Skyrama, a Bigpoint game. Not all features have been implemented, and the ones that are likely contain bugs. All help is welcome!

The way this server works is, least to say, kind of primitive. Data gets stored in JSON files directly on your pc instead of using a proper database. It does run just fine, however! In the future data storing might easily be upgraded if needed.

Keep in mind that although passwords should be properly encrypted/hashed, it is recommended to not use a password you use for any other services.


## Legal Issues

This repository is made for educational purposes only, and will not be monetized in any way. Contact me for any legal problems, and I'll take appropriate action.

## How to play

You can find the game on http://skyrama.glitch.me. You will either need a browser that supports Flash (and Flash Player itself), or an all-in-one browser like [Flash Browser](https://flash.pm).

## How to run the code locally

Install the libraries from requirements.txt and start server.py. It's as simple as that!

You will need a browser that supports Flash (and Flash Player itself) to run the game. Alternatively, you can use [Flash Browser](https://flash.pm).

## Known issues
- Leaving the tutorial early causes bugs.
- (and a bunch more xD)

## List of quest task types
This are all the types of tasks that can be in a quest. Doing an unimplemented one will work in-game, but after refreshing all further progress on quests will be gone! The tutorial (as well as the mid-game "cargo tutorial") and most important other types are working.

- [x] BuyBay
- [x] BuyLandsideBuilding
- [x] BuyPlane
- [x] CollectSouvenir
- [x] FillShop
- [x] GetAirCoins
- [x] GetCargo
- [x] GetPassengers
- [x] LandPlane
- [x] PlaceBay
- [x] PlaceCargoshop
- [ ] PlaceDecoration
- [ ] PlaceLandsideBuilding
- [x] PlaceTerminal
- [x] PlaceWarehouse
- [x] QuickStartPlane
- [x] ReturnPlane
- [x] SellProducts
- [x] SendPlane
- [ ] SendPlaneToStranger
- [ ] StoreLandsideBuilding
- [ ] StoreTerminal

## List of game commands
I'm not 100% sure if all of these are still being used in the latest version of Skyrama, but I hope it gives an indication of the progress of this private server.

- [x] general.getCv
- [x] general.getConfig
- [x] playerdata.updateBuddypingTime
- [x] playerdata.deleteBuddypingTime
- [x] account.getLatest
- [x] general.getInitState
- [x] general.soundIsOn
- [x] general.getBuddyInitState
- [x] playerdata.setLocation
- [x] playerdata.updateLevel
- [x] playerdata.updateSettings
- [ ] evoucher.book
- [x] lucky_luggage.spin
- [x] buddy.getAll
- [ ] buddy.collectPassenger
- [ ] buddy.receivePassengers
- [x] buddy.endRelationship
- [x] buddy.accept
- [x] buddy.decline
- [x] buddy.search
- [x] buddy.invite
- [x] planes.upgrade
- [x] planes.buy
- [x] planes.scrap
- [x] resource_items.buy  -  Only QS for now
- [x] packages.buy
- [x] planes.createFlyBy
- [x] planes.send
- [x] planes.sendback
- [x] planes.sendbackflyby
- [x] planes.miss
- [x] planes.removeFlyByPlane
- [x] planes.takeMeans
- [x] planes.setState
- [x] planes.get
- [x] planes.onStartCargoTutorial  -  Doesn't seem necessary?
- [x] backgrounds.buy
- [x] backgrounds.makeCurrent
- [x] landmarks.buy
- [x] landmarks.makeCurrent
- [x] bays.buy
- [x] cargoshops.fillShop
- [x] cargoshops.collectSalesRevenue
- [x] cargoshops.buy
- [x] cargoshops.buyCapacity
- [x] cargoshops.buyCargo
- [x] runways.buy
- [x] terminals.buy
- [ ] map_extensions.buy
- [ ] hangars.buy
- [x] hangars.upgrade
- [ ] warehouses.buy
- [x] playerdata.setbooster
- [x] landside_buildings.buy
- [x] landside_buildings.harvest
- [x] goals.buyTask
- [ ] souvenirs.takeReward
- [x] special_buildings.buy
- [x] placeable.place  -  PARTIALLY
- [x] placeable.setInStorage  -  PARTIALLY
- [x] flashCookies.set
- [ ] backgrounds.sell
- [x] bays.sell
- [ ] landmarks.sell
- [x] landside_buildings.sell
- [x] runways.sell
- [x] terminals.sell
- [ ] recycling.start
- [ ] recycling.instant
- [ ] recycling.collect
- [ ] crafting.processCraftingStep
- [ ] crafting.buyMaterials
- [ ] crafting.start
- [ ] crafting.instant
- [ ] crafting.collect
- [ ] crafting.buySlot
- [ ] general.trackFlashError
- [ ] materialevent.redeemItem

### Likely unused game commands
- account.getAll
- account.getData
- account.getRandom
- account.getDataByUserId
- buddy.getTutorialBuddy
- playerdata.getStats
- locations.get
- packets.get
- planes.changeFlightStatus
- planes.changeContainer
- backgrounds.get
- landmarks.get
- bays.get
- cargoshops.get
- runways.get
- terminals.get
- hangars.get
- warehouses.get
- landside_buildings.get
- souvenirs.buy

### Not sure what those are
- catchits.get
- catchits.catchPrize
- planes.rebateMiss
- offers.buyOffer
- expeditions.start
- expeditions.land
- expeditions.getanother
- expeditions.end
- expeditions.fillfuel
- expeditions.addfuel
