# Measurement Data Output Standard

This is the Herrick Laboratory psychrometric chamber experimental data standard.
The guidelines described here should be followed to the best of the
experimenter's ability when testing HVAC equipment in the psychrometric
chambers.

## Standard Measurement Labeling Convention

The goal of the measurement label is to describe the phsyical quantities
recorded during the experiment. The aim of the label is to record
_meta-information_ about the measurement. In other words, storing the:

* who,
* what,
* where,
* and how

of the measurement.  This is accomplished using a standard labeling convention
by the standards committee.  The standard labeling convention is described
below and its parts are described in individual sections henceforth.

    {COMPONENT}{#?}_{FLUID}{#?}_{LOCATION}{#?}_{TYPE}

The label stores information about the component, fluid, location, and type of
measurement being recorded.  Additionally, an optional numeric identifier can be
assigned to distiguish between multiple occurances of components or locations.
For example in a dual compressor systems, the compressors could be identified as
compressor 0 and compressor 1.

### Differential Measurements

Differential measurements are handled in a similar way to normal single point measurements.

However, each part of the namestring can now be composed of two parts - the distinction between 
first and second part is made by using a capital letter. Before the type, add "Delta" to specify
that a difference measurement is used. Naming scheme:

    {component1}{Componen2?}{#?}_{fluid1}{Fluid2?}{#?}_{location1}{Location2}{#?}_Delta{type1}{Type2?}

#### Examples:
Difference between compressor refrigerant inlet temperature and indoor heat exchanger (evaporator) refrigerant 
outlet temperature:

    idhxComp_ref_outIn_DeltaT
 
 Difference between air inlet temperature of evaporator and refrigerant inlet temperature:
    
    idhx_airRef_inIn_DeltaT

### Component Label Identifier

The component label identifier is used to describe which component in the
overall system the measurement is taken.  A list of acceptable component
identifiers is shown below.

<TABLE>
<CAPTION><EM>Acceptable component identifiers and descriptions.</EM></CAPTION>
<COLGROUP align="center">
<COLGROUP align="left">
<THEAD valign="top">
    <TR><TH>Identifier</TH><TH>Description</TH></TR>
<TBODY>
    <TR><TD>absr<TD>absorber</TR>
    <TR><TD>accm<TD>accumulator</TR>
    <TR><TD>ahu<TD>air handling unit</TR>
    <TR><TD>amb<TD>ambient</TR>
    <TR><TD>comp<TD>compressor</TR>
    <TR><TD>damp<TD>damper</TR>
    <TR><TD>desr<TD>desorber</TR>
    <TR><TD>eng<TD>engine/TR>
    <TR><TD>ehr<TD>electric heater</TR>
    <TR><TD>ejr<TD>ejector/injector</TR>
    <TR><TD>fan<TD>fan</TR>
    <TR><TD>filt<TD>filter</TR>
    <TR><TD>idhx<TD>indoor heat exchanger</TR>
    <TR><TD>ithx<TD>internal heat exchanger</TR>
    <TR><TD>mflr<TD>muffler</TR>
    <TR><TD>mot<TD>motor</TR>
    <TR><TD>noz<TD>nozzle box</TR>
    <TR><TD>odhx<TD>outdoor heat exchanger</TR>
    <TR><TD>pump<TD>pump</TR>
    <TR><TD>rect<TD>rectifier</TR>
    <TR><TD>recv<TD>receiver</TR>
    <TR><TD>sep<TD>separator</TR>
    <TR><TD>od<TD>outdoor</TR>
    <TR><TD>valv<TD>valve</TR>
    <TR><TD>rvalv<TD>reversing valve</TR>
    <TR><TD>vsd<TD>variable speed/frequency drive</TR>
    <TR><TD>xd<TD>expansion device</TR>
</TABLE>


### Fluid Label Identifier

The fluid label identifier is used to describe the "fluid" being measured by the
measurement device.  A list of acceptable fluid identifiers is shown below.

<TABLE>
<CAPTION><EM>Acceptable fluid identifiers and descriptions.</EM></CAPTION>
<COLGROUP align="center">
<COLGROUP align="left">
<THEAD valign="top">
    <TR><TH>Identifier</TH><TH>Description</TH></TR>
<TBODY>
    <TR><TD>air<TD>air</TR>
    <TR><TD>elec<TD>electric</TR>
    <TR><TD>gas<TD>natural gas</TR>
    <TR><TD>brn<TD>brine</TR>
    <TR><TD>h2o<TD>water</TR>
    <TR><TD>oil<TD>oil</TR>
    <TR><TD>ref<TD>refrigerant</TR>
    <TR><TD>rich<TD>rich solution</TR>
    <TR><TD>weak<TD>weak solution</TR>
    <TR><TD>mech<TD>mechanical, e.g. shaft or belt; what exactly needs to be clear from schematic</TR>
</TABLE>

### Location Label Identifier

The location label identifier is used to describe where on the component the
measurement is taken.  A list of acceptable location identifiers is shown below.

<TABLE>
<CAPTION><EM>Acceptable location identifiers and descriptions.</EM></CAPTION>
<COLGROUP align="center">
<COLGROUP align="left">
<THEAD valign="top">
    <TR><TH>Identifier</TH><TH>Description</TH><TH>Explanation</TH><TH>Example</TH></TR>
<TBODY>
    <TR>
        <TD>crct<TD>circuit
        <TD>Anywhere between the main inlet and outlet of heat exchangers
        <TD>odhx_ref_crct1_T is the temperature at a location marked as #1 
        within the refrigerant circuit of the outdoor heat exchanger
    </TR>
    <TR>
        <TD>ctrl<TD>controller
        <TD>Controller of a component
        <TD>fan_elec_ctrl_pwr is the power consumption of the fan controller
    </TR>
    <TR>
        <TD>dmp<TD>damper<TD>Damper of a component
        <TD>ahu_air_damp_pos is the opening position of the damper in 
        the air handling unit<TD>
    </TR>
    <TR><TD>exh<TD>exhaust<TD>Exhaust from a component<TD> ahu_air_exh_T is the temperature at the exhaust of the air handling unit</TR>
    <TR><TD>gasl<TD>gas line<TD>Gas line along the refrigerant circuit of a component<TD> odhx_ref_gasl_pg is the gage pressure at the exit towards the gas line of the system at the outdoor heat exchanger</TR>
    <TR><TD>in<TD>inlet<TD>Inlet of a component<TD> ithx_brn_in_T is the inlet brine temperature of an internal heat exchanger</TR>
    <TR><TD>int<TD>internal, interior<TD>Internal part of a component<TD> comp_ref_int1_pg is the gage pressure of the internal location #1 inside the compressor</TR>
    <TR><TD>idr<TD>indoor<TD>A location in the indoor room around a component<TD> ahu_air_indr_B is the indoor room wet-bulb temperature around the air handling unit</TR>
    <TR><TD>lvl<TD>level<TD><TD></TR>
    <TR>
        <TD>liql<TD>liquid line
        <TD>Liquid line along the refrigerant circuit of a component
        <TD> odhx_ref_liql_pg is the gage pressure at the exit towards 
        the liquid line at the outdoor heat exchanger
    </TR>
    <TR><TD>mix<TD>mixed<TD>Mixing chamber inside a component<TD> ahu_air_mix_D is the dewpoint at the mixing chamber inside the air handling unit</TR>
    <TR><TD>odr<TD>outdoor<TD>A location around the outdoor room at a component<TD> comp_air_odr_T is the temperature around the compressor in the outdoor room</TR>
    <TR><TD>out<TD>outlet<TD>Outlet of a component<TD>xd2_ref_out_pg is the gage pressure at the refrigerant outlet of expansion valve #2</TR>
    <TR><TD>phas<TD>phase<TD>Phase of power supply to a component<TD>comp_elec_phas2_I is the current at the second phase of the electrical power supply to the compressor</TR>
    <TR><TD>plnm<TD>plenum<TD>Plenum of a component<TD>idhx_air_plenum_D is the dewpoint at the plenum of the indoor unit heat exchanger</TR>
    <TR><TD>ret<TD>return<TD>Return air duct of a component<TD>ahu_air_ret_B is the air wet-bulb temperature at the return air pipe of the air handling unit</TR>
    <TR><TD>sply<TD>supply<TD>Supply air duct of a component<TD>ahu_air_sply_RH is the air relative humidity at the supply air pipe of the air handling unit</TR></TR>
    <TR><TD>srnd<TD>surroundings<TD>Surroundings of the psychrometric chamber<TD> noz_air_srndInt_DeltaP is the air pressure difference between the atmosphere and the interior of the nozzle box</TR>
</TABLE>

### Measurement Type Label Identifier

The measurement type label identifier is used to describe the actual type of
measurement being recorded.  A list of acceptable measurement types is shown
below.

<TABLE>
<CAPTION><EM>Acceptable measurement type identifiers and
             descriptions.</EM></CAPTION>
<COLGROUP align="center">
<COLGROUP align="left">
<THEAD valign="top">
    <TR><TH>Identifier</TH><TH>Description</TH><TH>Explanation</TH><TH>Example</TH></TR>
<TBODY>
    <TR>
        <TD>B<TD>wet bulb<TD>Wet bulb for humid air.
        <TD>idhx_air_in_B is indoor air heat ezxchanger inlet wet bulb temperature.
    </TR>
    <TR>
        <TD>D<TD>dew point<TD>Dewpoint for humid air
        <TD>idhx_air_in_D is indoor air heat ezxchanger inlet dry bulb temperature.
    </TR>
    <TR>
        <TD>duty<TD>PWM duty cycle
        <TD>Duty cycle for PWM (pulse-width-modulation) type signals.
        <TD>xd_ref_liql_PWM is the duty cycle of a pulse width modulated electronic 
	expansion valve.
    </TR>
    <TR>
        <TD>freq<TD>frequency
        <TD>Frequency of a component.
        <TD>vsd_elec_out_freq is the output frequency of a variable speed drive.
    </TR>
    <TR>
        <TD>I
        <TD>current
        <TD>Electrical current.
        <TD> vsd_elec_out_I is the output current of a variable speed drive 
             and typically equivalent to comp_elec_in_I. 
    </TR>
    <TR>
        <TD>T
        <TD>temperature
        <TD>Temperature.
        <TD>comp_ref_out_T is the refrigerant temperature at the outlet of the 
	compressor.
    </TR>
    <TR>
        <TD>mdot
        <TD>mass flow rate
        <TD>Mass flow rate.
        <TD>comp_ref_out_mdot is the refrigerant outlet flowrate and is 
	different from comp_ref_in_mdot if vapor injected compression is used.
    </TR>
    <TR>
        <TD>pa
        <TD>absolute pressure
        <TD>Absolute pressure measurement.
        <TD>comp_ref_out_pa is the absolute refrigerant outlet pressure of the 
	compressor if an absolute pressure transducer was used. 
    </TR>
    <TR>
        <TD>pag
        <TD>absolute pressure, based on gauge pressure measurement
        <TD>Gauge pressure measurement converted to absolute 
	pressure at the time of measurement.
        <TD>comp_ref_out_pag is the absolute refrigerant outlet pressure of the 
	compressor if a gauge pressure transducer was used and the value is 
	already containing the compensation for the ambient pressure.
    </TR>
    <TR>
        <TD>Delta{type1}{Type2?}
        <TD>Pressure difference between two points, see Differential Measurements.
        <TD><TD>idhxComp_ref_outIn_DeltaT is the difference between compressor 
	refrigerant inlet temperature and indoor heat exchanger (evaporator) 
	refrigerant outlet temperature
    </TR>
    <TR>
        <TD>pg
        <TD>gauge pressure
        <TD>Gauge pressure measurement.
        <TD> comp_ref_out_pg is the gauge refrigerant outlet pressure of the 
	compressor if a gauge pressure transducer was used. 
    </TR>
    <TR>
        <TD>pos
        <TD>position
        <TD>Position of an adjustable component.
        <TD> ahu_air_damp_pos is the opening position of the damper in the air 
	handling unit.
    </TR>
    <TR>
        <TD>pwr
        <TD>power
        <TD>Electrical power.
        <TD>Comp_elec_in_power is the input power of the compressor. Note: do 
	not use power for mechanical measurements, rather report RPM and torque.
    </TR>
    <TR>
        <TD>RH
        <TD>relative humidity
        <TD>Relative humidity of air.
        <TD>idhx_air_out_RH is the relative humidity of the air leaving the 
	evaporator.
    </TR>
    <TR>
        <TD>spd
        <TD>rotational speed
        <TD>Rotational speed of a component.
        <TD> comp_mech_int_speed is the rotational speed of the compressor and 
	typically different from comp_elec_in_freq.
    </TR>
    <TR>
        <TD>sw
        <TD>switch
        <TD>State of a switch.
        <TD>sep_oil_lvl_sw is the state of the liquid level switch in the oil 
	separator.
    </TR>
    <TR>
        <TD>u
        <TD>flow velocity
	<TD>Flow velocity of a fluid.
        <TD>idhx_air_in_u is the indoor heat exchanger inlet flow velocity.
    </TR>
    <TR>
        <TD>V
        <TD>voltage
        <TD>Electrical voltage.
        <TD>fan_elec_in_V is the electrical voltage of the indoor fan power.
    </TR>
    <TR>
        <TD>Vdot
        <TD>volumetric flow rate
        <TD>Volumetric flow rate of a fluid
        <TD>noz_air_in_Vdot is the flow rate measured by the flow measurement
	nozzle box.
    </TR>
</TABLE>

    
### Example Systems

Here is a list of systems with their sensors labeled as examples.

#### Refrigerant circuit of a ductless split heat pump system

Ductless split heat pump system is a split system which can provide heating or cooling to a building zone. It operates with a compressor, a reversing valve, an indoor heat exchanger, an electronic expansion valve, an outdoor heat exchanger and an accumulator. The indoor heat exchanger is housed inside the indoor unit while the other components are housed in the outdoor unit. The reversing valve controls the refrigerant flow to provide either heating or cooling to the building zone.

In this example, an experiment was designed to measure the states of refrigerant between components and the refrigerant mass flow rate of the system. The schematic of the sensor location is given as follows.

<img src="https://raw.github.com/ahjortland/psychroom/master/docs/DHP.png" alt="DHP_ref_fig" title="DHP_ref_fig" style="width: 500px;"/>

In the schematic, the indoor unit is named as ahu1 and the outdoor unit is named as ahu2. M stands for refrigerant mass flowmeter, T stands for immersion thermocouples, P stands for gage pressure transducers and W stands for a power transducer. The heat exchangers in the system are not labeled as condenser and evaporator because both heat exchangers can serve as a condenser or an evaporator. The power transducers are positioned next to the indoor unit and outdoor unit labels as they are measuring power consumption of the indoor units and outdoor units but not the power consumption of the individual components. The refrigerant on the right-handed side of the heat exchangers are always in vapor form and the pipes on that side are the gas line while other pipes are called the liquid line. The location of liquid line and gas line and the refrigerant flow direction are indicated in the legend in the diagram.

The labeling of the sensors is listed as follows.

<TABLE>
<CAPTION><EM>Name and labels of sensors in the ductless split heat pump system</EM></CAPTION>
<COLGROUP align="center">
<COLGROUP align="left">
<THEAD valign="top">
    <TR><TH>Sensor</TH><TH>Label</TH><TH>Explanation</TH></TR>
<TBODY>
    <TR><TD>T at the compressor discharge<TD>comp_ref_out_T<TD></TR>
    <TR><TD>T at the indoor heat exchanger gas line exit<TD>idhx_ref_gasl_T<TD></TR>
    <TR><TD>T at the indoor heat exchanger liquid line exit<TD>idhx_ref_liql_T<TD></TR>
    <TR><TD>T at the expansion valve liquid line exit<TD>xd_ref_liql_T<TD>Only one location refers to the expansion valve so no number is needed</TR>
    <TR><TD>T at the outdoor heat exchanger liquid line exit<TD>odhx_ref_liql_T<TD></TR>
    <TR><TD>T at the outdoor heat exchanger gas line exit<TD>odhx_ref_gasl_T<TD></TR>
    <TR><TD>T at the accumulator inlet<TD>accm_ref_in_T<TD></TR>
    <TR><TD>T at the compressor suction<TD>comp_ref_in_T<TD></TR>
    <TR><TD>P at the compressor discharge<TD>comp_ref_out_pg<TD></TR>
    <TR><TD>P at the indoor heat exchanger gas line exit<TD>idhx_ref_gasl_pg<TD></TR>
    <TR><TD>P at the indoor heat exchanger liquid line exit<TD>idhx_ref_liql_pg<TD></TR>
    <TR><TD>P at the expansion valve liquid line exit<TD>xd_ref_liql_pg<TD>Only one location refers to the expansion valve so no number is needed</TR>
    <TR><TD>P at the outdoor heat exchanger liquid line exit<TD>odhx_ref_liql_pg<TD></TR>
    <TR><TD>P at the outdoor heat exchanger gas line exit<TD>odhx_ref_gasl_pg<TD></TR>
    <TR><TD>P at the accumulator inlet<TD>accm_ref_in_pg<TD></TR>
    <TR><TD>P at the compressor suction<TD>comp_ref_in_pg<TD></TR>
    <TR><TD>M at the indoor unit heat exchanger liquid line exit<TD>idhx_ref_liql_mdot<TD></TR>
    <TR><TD>W at the indoor unit<TD>ahu1_elec_idr_pwr<TD>The indoor unit is labeled as ahu1 and idr means that the power transducer is positioned in the indoor room.</TR>
    <TR><TD>W at the outdoor unit<TD>ahu2_elec_idr_pwr<TD>The outdoor unit is labeled as ahu2 and odr means that the power transducer is positioned in the indoor room.</TR>
</TABLE>

## Measurement Data Output File Format

### File Header Information

What do we put in the header?
