# True vs Magnetic North

## Objective
To understand the difference between magnetic north and true north, quantify the angular gap called magnetic declination, and implement methods to correctly convert compass bearings to true bearings to prevent navigation errors.

## Dependencies and prerequisites
*   Clear night sky (for Polaris comparison).
*   Sunny day, a shadow stick, flat ground, and a compass (for solar noon measurement).
*   Clear horizon at sunrise and sunset (for sunrise/sunset averaging).
*   A functioning compass.

## Material
*   **Two Norths:** True north (geographic north, where the rotational axis intersects the surface) and magnetic north (where the compass needle points).
*   **Magnetic Declination:** The angular difference between true north and magnetic north, ranging from 0 degrees to over 25 degrees east or west.
*   **Local Anomalies:** Magnetic anomalies caused by iron ore deposits, volcanic rock, or underground mineral veins that distort compass readings independently of regional declination.
*   **Secular Variation:** The slow change in declination over time (typically 0.1-0.2 degrees per year).

### Declination by World Region (Approximate Mid-2020s Values)
| Region                         | Approximate Declination | Direction                                                         |
| ------------------------------ | ----------------------- | ----------------------------------------------------------------- |
| Eastern United States          | 5-15 degrees            | West                                                              | 
| Western United States         | 10-18 degrees           | East                                                              | 
| Central Europe                 | 0-5 degrees             | East                                                              | 
| United Kingdom                 | 0-3 degrees             | West (decreasing toward 0)                                        |
| Eastern Siberia                | 5-15 degrees            | West                                                              | 
| Eastern Australia              | 8-13 degrees            | East                                                              | 
| Western Australia             | 0-5 degrees             | West                                                              | 
| Southern Africa                | 15-25 degrees           | West                                                              | 
| Brazil                         | 15-22 degrees           | West                                                              | 
| Alaska                         | 10-25 degrees           | East                                                              | 
| Agonic line (zero declination) | 0 degrees               | Runs roughly through the US Midwest, down through Central America |

## System
The system relies on distinguishing between the fixed geographic orientation (True North) and the localized magnetic field orientation (Magnetic North).

### Magnetic Dip (Inclination)
*   **Definition:** The Earth’s magnetic field is not horizontal; field lines angle downward into the Earth.
*   **Dip Values:** 0 degrees at the magnetic equator (horizontal) and 90 degrees at the magnetic poles (plunges straight down).
*   **Impact:** In a pivot or suspended compass, a magnetized needle may tilt due to the dip. 
*   **Solutions for Dip:** Balance the needle slightly off-center to counteract gravity, or add a small counterweight to the north-dipping end (in the Northern Hemisphere).

## Technology
*   **Compass:** The primary tool that points to magnetic north.
*   **Polaris Sightline:** Used to establish true north.
*   **Shadow Stick:** Used to determine true north/south at solar noon.
*   **Protractor/Correction Board:** A physical tool for creating and displaying declination corrections.

## Tools
*   Compass
*   Polaris
*   Shadow Stick
*   Correction Board (for permanent settlements)

## Process
### Measuring Local Declination
**Method 1: Polaris Comparison (Most Accurate)**
1. Locate Polaris using the Big Dipper’s pointer stars.
2. Face Polaris directly (True North).
3. Note where the compass needle points relative to Polaris.
4. The angle between the needle and the sightline is the local declination.

**Method 2: Solar Noon Shadow Stick**
1. Set up a shadow stick on flat ground.
2. At solar noon (shortest shadow), the shadow points exactly true north/south.
3. Compare this true-north line with the compass reading.
4. The angular difference is the declination.

**Method 3: Sunrise/Sunset Averaging**
1. On the equinox, take compass bearings at sunrise and sunset.
2. Average the two bearings to approximate declination.

### Applying Declination Corrections
**Rule Set (The Memory Aid):**
*   **East Declination (Magnetic North is East of True North):**
    *   Compass to true: Subtract the declination.
    *   True to compass: Add the declination.
*   **West Declination (Magnetic North is West of True North):**
    *   Compass to true: Add the declination.
    *   True to compass: Subtract the declination.

### Building a Declination Reference Tool
1. **Establish a True North Marker:** Drive two stakes aligned with Polaris to define a true north line.
2. **Mark the Magnetic Bearing:** Stand at the southern stake and take a compass reading along the line to the northern stake. The difference from 360/0 degrees is the declination.
3. **Create a Correction Board:** Mark true north and magnetic north lines with the declination angle clearly labeled.
4. **Update Annually:** Re-measure using Polaris and update the correction board.

## Notes
*   Declination errors can accumulate significantly over long distances (e.g., 15 degrees over 30 km results in nearly 8 km error).
*   When declination does not matter: Correction is unnecessary for following a back-bearing, navigating between visible landmarks, relative bearings when mapping local areas, or small distances (under 1 km).
*   Magnetic dip is a concern for pivoted or suspended compasses but is managed by balancing or counterweight.
