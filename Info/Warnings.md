## No run found in bidsmap. Looking into template

```
mapper(73) - WARNING MRI/001-localizer/0: No run found in bidsmap. Looking into template
```

During map creation step, `bidsme` found a new file
(here `MRI/001-localizer/0`, first file in
`001-localizer` series),
that it could identify using template.
A new section, corresponding to the image in question
is automatically placed into `bidsmap.yaml` file.

**Action required:**
Identify the new section in `bidsmap.yaml`, and:

 1. change `template: true` to `template: false`
 2. Verify that section is placed under correct modality (`anat`, `fmap` etc.), if not, move it to correct one
 3. Verify the `suffix` field, and correct if needed
 3. If `bids` and `json` subsection are automatically filled, verify and correct any errors
 4. If `bids` and `json` are empy (`bids: !!omap[]`), leave it empty, on next iteration it will be automatically filled for a given modality - suffix configuration
 
## Placeholder found

```
bidsme.Modules.base(901) - WARNING 002-cmrr_mbep2d_bold_mb2_invertpe/4: Placehoder found
```

One of the sections in `bidsmap.yaml` contains `<<placeholder>>` tag.
This tag represents fields that are required by BIDS.

**Action required:**
Identify the section in question (search for series id in the warning message, or just search for `placeholder`), and replace placeholder by required value.

## Also checks run

```
bidsmap._bidsmap(201) - WARNING fmap/0: also checks run: fmap/1
```

When same image matches several section in `bidsmap.yaml`,
bidsme creates this warning.
The main goal is to prevent the shadowing of sections.
Usually, it happens when a new section is generated automatically, with default `attributes` subsection.

**Action required:**
Identify the duplicated sections and fix the `attributes`
subsection.
Usually such sections don't have filled `provenance`
field.

##  Naming schema not BIDS

```
Modules.base(1137) - WARNING 002-al_mtflash3d_sensArray/0: Naming schema not BIDS
```

`bidsme` have an internal reference on how a given
image expected to be formatted. 
If the current bidsification deviates from it,
for example, there an additional entity, `bidsme`
will warn about.

**Action requires:**
Just cross-check the corresponding `bids` subsection.
If you are sure that the schema is correct, then
you just need to manually change `checked` from
`false` to `true`. It will silence the warning.

## Can't find an attirbute

```
bidsme.Modules.base(619) - WARNING 004-al_mtflash3d_PDw/0: Can't find 'ScanOptions' attribute from '<ScanOptions>'
```

This warning tells that `bidsme` can't retrieve a given
attribute (here `<ScanOptions>`).
The causes may be multiples, from a misspell in the
name of attribute to simply the lack of the attribute
in the header.

**Action requires:**
If this warning appears in the section generated from
template, it can be safely ignored, the warning
will disapear at the next iteration of mapping stage.
If the warning persists, then you should check the
spelling of the attribute or replace it by a value.

