
# Skyrama Private Server

A simple server for the game Skyrama. Not all features have been implemented, and the ones that are may contain bugs. All help is welcome :)

Besides that, keep in mind that passwords are not properly encrypted at the moment! So I highly recommend you choose a unique password you DON'T use for any other services.


## Legal Issues

This repository is made for educational purposes only, and will not be monetized in any way. Contact me for any legal problems, and I'll take appropriate action.

## How to play

You can find the game on http://skyrama.glitch.me. You will need a browser that supports flash (and flash player itself) to run the game. I personally recommend https://flash.pm/browser/ if you want to do it the easy way.

## How to run the code locally

In order to run the code, simply run server.py. Make sure you have installed the required libraries from requirements.txt first.

You will need a browser that supports Flash (and Flash Player itself) to run the game. Alternatively, you can use https://flash.pm/browser/.

## Known issues
- Leaving the tutorial early causes bugs.

## List of quest task types
This are all the types of tasks that can be in a quest. Doing an unimplemented one will work in-game, but after refreshing, all further progress on quests will be gone! The tutorial (as well as the mid-game "cargo tutorial") and most important other types are working.

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
- [ ] playerdata.updateBuddypingTime
- [ ] playerdata.deleteBuddypingTime
- [x] account.getLatest  -  PARTIALLY
- [x] general.getInitState
- [x] general.soundIsOn
- [ ] general.getBuddyInitState
- [x] playerdata.setLocation
- [x] playerdata.updateLevel
- [x] playerdata.updateSettings
- [ ] evoucher.book
- [x] lucky_luggage.spin
- [x] buddy.getAll
- [ ] buddy.getTutorialBuddy
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
- [ ] resource_items.buy
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
- [ ] backgrounds.buy
- [ ] backgrounds.makeCurrent
- [ ] landmarks.buy
- [ ] landmarks.makeCurrent
- [x] bays.buy
- [x] cargoshops.fillShop
- [x] cargoshops.collectSalesRevenue
- [ ] cargoshops.buy
- [ ] cargoshops.buyCapacity
- [ ] cargoshops.buyCargo
- [x] runways.buy
- [x] terminals.buy
- [ ] map_extensions.buy
- [ ] hangars.buy
- [ ] hangars.upgrade
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
- [ ] bays.sell
- [ ] landmarks.sell
- [ ] landside_buildings.sell
- [ ] runways.sell
- [ ] terminals.sell
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
