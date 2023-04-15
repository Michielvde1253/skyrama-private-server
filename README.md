
# Skyrama Private Server

A simple server for the game Skyrama. Not all features have been implemented, and the ones that are may contain bugs. All help is welcome :)

Besides that, keep in mind that passwords are not properly encrypted at the moment! So I highly recommend you choose a unique password you DON'T use for any other services.


## Legal Issues

This repository is made for educational purposes only, and will not be monetized in any way. Contact me for any legal problems, and I'll take appropriate action.

## How to play

You can find the game on https://skyrama.glitch.me. To play, you will need a browser that supports flash (and flash player itself) to run the game. I personally recommend https://flash.pm/browser/ if you want to do it the easy way.

## How to run the code locally

In order to run the code, simply download the .zip from Github and run server.py. Make sure you have installed the required libraries from requirements.txt first.

You will need a browser that supports Flash (and Flash Player itself) to run the game. Alternatively, you can use https://flash.pm/browser/.

## Known issues
- Leaving the tutorial early causes bugs.
- Quests sometimes give items or buildings, which is currently unimplemented.
- Sometimes instand start/land is not being handled by the server (giving you back the aircash).

## List of game commands
I'm not 100% sure if all of these are still being used in the latest version of Skyrama, but I hope it gives an indication of the progress of this private server.

- [x] general.getCv
- [x] general.getConfig
- [ ] account.getData
- [ ] playerdata.updateBuddypingTime
- [ ] playerdata.deleteBuddypingTime
- [ ] account.getDataByUserId
- [x] account.getAll
- [ ] account.getRandom
- [x] account.getLatest  -  PARTIALLY
- [x] general.getInitState
- [x] general.soundIsOn
- [ ] general.getBuddyInitState
- [ ] playerdata.getStats
- [x] playerdata.setLocation
- [ ] playerdata.updateLevel
- [x] playerdata.updateSettings
- [ ] locations.get
- [ ] evoucher.book
- [x] lucky_luggage.spin
- [ ] catchits.get
- [ ] catchits.catchPrize
- [x] buddy.getAll
- [ ] buddy.getTutorialBuddy
- [ ] buddy.collectPassenger
- [ ] buddy.receivePassengers
- [x] buddy.endRelationship
- [x] buddy.accept
- [x] buddy.decline
- [x] buddy.search
- [x] buddy.invite
- [ ] packets.get
- [x] planes.upgrade
- [x] planes.buy
- [x] planes.scrap
- [ ] resource_items.buy
- [x] packages.buy
- [ ] planes.createFlyBy
- [x] planes.send
- [x] planes.sendback
- [ ] planes.sendbackflyby
- [ ] planes.prepare
- [x] planes.miss
- [ ] planes.removeFlyByPlane
- [x] planes.takeMeans
- [ ] planes.rebateMiss
- [x] planes.setState
- [x] planes.get
- [ ] planes.changeFlightStatus
- [ ] planes.changeContainer
- [ ] planes.onStartCargoTutorial
- [ ] backgrounds.get
- [ ] backgrounds.buy
- [ ] backgrounds.makeCurrent
- [ ] landmarks.get
- [ ] landmarks.buy
- [ ] landmarks.makeCurrent
- [ ] bays.get
- [x] bays.buy
- [ ] cargoshops.get
- [ ] cargoshops.fillShop
- [ ] cargoshops.collectSalesRevenue
- [ ] cargoshops.buy
- [ ] cargoshops.buyCapacity
- [ ] cargoshops.buyCargo
- [ ] runways.get
- [x] runways.buy
- [ ] terminals.get
- [x] terminals.buy
- [ ] map_extensions.buy
- [ ] hangars.get
- [ ] hangars.buy
- [ ] hangars.upgrade
- [ ] warehouses.get
- [ ] warehouses.buy
- [x] playerdata.setbooster
- [ ] landside_buildings.get
- [x] landside_buildings.buy
- [x] landside_buildings.harvest
- [ ] goals.buyTask
- [ ] offers.buyOffer
- [ ] souvenirs.buy
- [ ] souvenirs.takeReward
- [x] special_buildings.buy
- [x] placeable.place  -  PARTIALLY
- [x] placeable.setInStorage  -  PARTIALLY
- [ ] expeditions.start
- [ ] expeditions.land
- [ ] expeditions.getanother
- [ ] expeditions.end
- [ ] expeditions.fillfuel
- [ ] expeditions.addfuel
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
