# Project Brief
This project implements the Smart Parking System prototype for the City of Moondalup, built as part of a smart city
initiative.

* This project uses sensors and displays to:
* Track parking bay availability in real time in uncontrolled car parks
* Show available bays, ambient temperature, and community announcements on digital displays
* Store scanned vehicle licence plates for reference
* Update information promptly as cars enter and exit

## Evidence
![Initial commit](screenshots/image-of-github-after-push.png)

### 2.3
| Class Name | Attributes | Methods |
|------------|------------|---------|
| CarPark    |            |         |
| Sensor     |            |         |
| Display    |            |         |

### 2.4.3
![Added stubs for classes](screenshots/stubs-for-classes.png)

### 2.5.4
![Git Tags](screenshots/git-tags.png)

### 2.7.3

> Q: Which class is responsible for the number of available bays (and why)?
> The CarPark class should manage the information displayed by the displays. The Display class should only be
> responsible for displaying information, not deciding what to display. This avoids the displays showing different
> information as they would need to decide when to fetch data from the CarPark and other APIs such as a weather API
> in order to display information. Whereas the CarPark can signal to the displays when to update when a change occurs.
> 
> Q: Which class is responsible for the current temperature (and why)?
> None of the classes are responsible for this. A new class implementing a weather or temp sensor should be implemented
> instead, depending on the CTO's requirements.
> 
> Q: Which class is responsible for the time (and why)?
> None of the classes are responsible for the time, however, python has an inbuilt datetime which can provide the
> current time. So the class responsible for what is displayed (CarPark), can and should call this when determining what
> to display

![Added methods to the car park class](screenshots/methods-to-car-park.png)