## Bidsified name same as first file of recording

```
mapper(105) - ERROR MRI/002-cmrr_mbep2d_bold_mb2_invertpe/1: Bidsified name same as first file of recording: fmap/sub-001_ses-s01512_acq-nBack_dir-PA_epi
```

This error is raised when two or more images from the same series will have same bidsified name.
Typically it happens when a given series (here `MRI/002-cmrr_mbep2d_bold_mb2_invertpe`) is composed of several images, but this is not represented in the `bids` subsection in the corresponding section of `bidsmap.yaml`.

**Action required:**
Find the metadata which allow to distinguish between different images (typically `<AcquisitionNumber>` for MRI), and insert this field into appropriate entity in `bids` subsection (`run` or `vol`).

## Matched example of already processed run

```
mapper(382) - ERROR Matches example of already processed run fmap/sub-001_ses-s01512_acq-nBack_dir-PA_run-001_epi
```

This error is raised when a new series is processed
(look the log line just above the error), but have the same bidsified name as previouslu processed image
(here `fmap/sub-001_ses-s01512_acq-nBack_dir-PA_run-001_epi`).
Typically it happens when `attributes` subsection is not
specific enought, and making two different series match
the sema section.

**Action required:**
Find the metadata which allow to distinguish images
from the different series, for ex. `<ImageType>`, 
`<SeriesDescription>`, or `<SeriesNumber>`,
and adapt `atributes` subsection, so images from only
one series will be matched by a given section.