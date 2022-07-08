from imageio.config import known_plugins, known_extensions, PluginConfig, FileExtension

# Register the FreeImage Plugin
FREEIMAGE_FORMATS = [
    (
        "BMP",
        0,
        "Windows or OS/2 Bitmap",
        ".bmp",
        "i",
        "FreeimageBmpFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "CUT",
        21,
        "Dr. Halo",
        ".cut",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "DDS",
        24,
        "DirectX Surface",
        ".dds",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "EXR",
        29,
        "ILM OpenEXR",
        ".exr",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "G3",
        27,
        "Raw fax format CCITT G.3",
        ".g3",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "GIF",
        25,
        "Static and animated gif (FreeImage)",
        ".gif",
        "iI",
        "GifFormat",
        "imageio.plugins.freeimagemulti",
    ),
    (
        "HDR",
        26,
        "High Dynamic Range Image",
        ".hdr",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "ICO",
        1,
        "Windows Icon",
        ".ico",
        "iI",
        "IcoFormat",
        "imageio.plugins.freeimagemulti",
    ),
    (
        "IFF",
        5,
        "IFF Interleaved Bitmap",
        ".iff .lbm",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "J2K",
        30,
        "JPEG-2000 codestream",
        ".j2k .j2c",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "JNG",
        3,
        "JPEG Network Graphics",
        ".jng",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "JP2",
        31,
        "JPEG-2000 File Format",
        ".jp2",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "JPEG",
        2,
        "JPEG - JFIF Compliant",
        ".jpg .jif .jpeg .jpe",
        "i",
        "FreeimageJpegFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "JPEG-XR",
        36,
        "JPEG XR image format",
        ".jxr .wdp .hdp",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "KOALA",
        4,
        "C64 Koala Graphics",
        ".koa",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    # not registered in legacy pillow
    # ("MNG", 6, "Multiple-image Network Graphics", ".mng", "i", "FreeimageFormat", "imageio.plugins.freeimage"),
    (
        "PBM",
        7,
        "Portable Bitmap (ASCII)",
        ".pbm",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "PBMRAW",
        8,
        "Portable Bitmap (RAW)",
        ".pbm",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "PCD",
        9,
        "Kodak PhotoCD",
        ".pcd",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "PCX",
        10,
        "Zsoft Paintbrush",
        ".pcx",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "PFM",
        32,
        "Portable floatmap",
        ".pfm",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "PGM",
        11,
        "Portable Greymap (ASCII)",
        ".pgm",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "PGMRAW",
        12,
        "Portable Greymap (RAW)",
        ".pgm",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "PICT",
        33,
        "Macintosh PICT",
        ".pct .pict .pic",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "PNG",
        13,
        "Portable Network Graphics",
        ".png",
        "i",
        "FreeimagePngFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "PPM",
        14,
        "Portable Pixelmap (ASCII)",
        ".ppm",
        "i",
        "FreeimagePnmFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "PPMRAW",
        15,
        "Portable Pixelmap (RAW)",
        ".ppm",
        "i",
        "FreeimagePnmFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "PSD",
        20,
        "Adobe Photoshop",
        ".psd",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "RAS",
        16,
        "Sun Raster Image",
        ".ras",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "RAW",
        34,
        "RAW camera image",
        ".3fr .arw .bay .bmq .cap .cine .cr2 .crw .cs1 .dc2 "
        ".dcr .drf .dsc .dng .erf .fff .ia .iiq .k25 .kc2 .kdc .mdc .mef .mos .mrw .nef .nrw .orf "
        ".pef .ptx .pxn .qtk .raf .raw .rdc .rw2 .rwl .rwz .sr2 .srf .srw .sti",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "SGI",
        28,
        "SGI Image Format",
        ".sgi .rgb .rgba .bw",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "TARGA",
        17,
        "Truevision Targa",
        ".tga .targa",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "TIFF",
        18,
        "Tagged Image File Format",
        ".tif .tiff",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "WBMP",
        19,
        "Wireless Bitmap",
        ".wap .wbmp .wbm",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "WebP",
        35,
        "Google WebP image format",
        ".webp",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "XBM",
        22,
        "X11 Bitmap Format",
        ".xbm",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
    (
        "XPM",
        23,
        "X11 Pixmap Format",
        ".xpm",
        "i",
        "FreeimageFormat",
        "imageio_freeimage.freeimage",
    ),
]
for name, i, des, ext, mode, class_name, module_name in FREEIMAGE_FORMATS:
    config = PluginConfig(
        name=name.upper() + "-FI",
        class_name=class_name,
        module_name=module_name,
        is_legacy=True,
        install_name="freeimage",
        legacy_args={
            "description": des,
            "extensions": ext,
            "modes": mode,
            "fif": i,
        },
    )
    known_plugins[config.name] = config
