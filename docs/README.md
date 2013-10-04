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

    {COMPONENT}{#?}_{FLUID}_{LOCATION}{#?}_{TYPE}

The label stores information about the component, fluid, location, and type of
measurement being recorded.  Additionally, an optional numeric identifier can be
assigned to distiguish between multiple occurances of components or locations.
For example in a dual compressor systems, the compressors could be identified as
compressor 0 and compressor 1.

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
    <TR><TD>ahu<TD>air handling unit</TR>
    <TR><TD>cmp<TD>compressor</TR>
    <TR><TD>ihx<TD>indoor heat exchanger</TR>
    <TR><TD>ohx<TD>outdoor heat exchanger</TR>
    <TR><TD>idf<TD>indoor fan</TR>
    <TR><TD>odf<TD>outdoor fan</TR>
    <TR><TD>exv<TD>expansion valve</TR>
    <TR><TD>oae<TD>outdoor-air economizer</TR>
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
    <TR><TD>ref<TD>refrigerant</TR>
    <TR><TD>air<TD>air</TR>
    <TR><TD>oil<TD>oil</TR>
    <TR><TD>elec<TD>electrical</TR>
    <TR><TD>gly<TD>glycol</TR>
</TABLE>

### Location Label Identifier

The location label identifier is used to describe where on the component the
measurement is taken.  A list of acceptable location identifiers is shown below.

<TABLE>
<CAPTION><EM>Acceptable location identifiers and descriptions.</EM></CAPTION>
<COLGROUP align="center">
<COLGROUP align="left">
<THEAD valign="top">
    <TR><TH>Identifier</TH><TH>Description</TH></TR>
<TBODY>
    <TR><TD>ret<TD>return</TR>
    <TR><TD>mix<TD>mixed</TR>
    <TR><TD>out<TD>outdoor</TR>
    <TR><TD>sup<TD>supply</TR>
    <TR><TD>in<TD>inlet</TR>
    <TR><TD>out<TD>outlet</TR>
    <TR><TD>vfd<TD>variable frequncy drive</TR>
    <TR><TD>ctl<TD>controller</TR>
    <TR><TD>gas<TD>gas line</TR>
    <TR><TD>liq<TD>liquid line</TR>
    <TR><TD>ckt<TD>circuit</TR>
</TABLE>

# Measurement Type Label Identifier

The measurement type label identifier is used to describe the actual type of
measurement being recorded.  A list of acceptable measurement types is shown
below.

<TABLE>
<CAPTION><EM>Acceptable location identifiers and descriptions.</EM></CAPTION>
<COLGROUP align="center">
<COLGROUP align="left">
<THEAD valign="top">
    <TR><TH>Identifier</TH><TH>Description</TH></TR>
<TBODY>
    <TR><TD>T<TD>absolute temperature</TR>
    <TR><TD>P<TD>absolute pressure</TR>
    <TR><TD>Pg<TD>gage pressure</TR>
    <TR><TD>dP<TD>differential pressure</TR>
    <TR><TD>W<TD>power</TR>
    <TR><TD>F<TD>frequency</TR>
    <TR><TD>V<TD>voltage</TR>
    <TR><TD>I<TD>current</TR>
    <TR><TD>R<TD>relative humidity</TR>
    <TR><TD>D<TD>dew point</TR>
    <TR><TD>B<TD>wet bulb</TR>
</TABLE>
