# coding: utf-8
import unreal


editor_util = unreal.GlobalEditorUtilityBase.get_default_object()
assets = editor_util.get_selected_assets()

#获取材质通道
materials = unreal.EditorFilterLibrary.by_class(assets, unreal.Material)

for material in  materials:
    #Base Color-基础颜色
    texturesample = unreal.MaterialEditingLibrary.create_material_expression(
        material,
        unreal.MaterialExpressionTextureSampleParameter2D,
        -200,
        0
    )
    texturesample.set_editor_property("parameter_name","Base Color Texture")
    unreal.MaterialEditingLibrary.connect_material_property(
        texturesample,
        'rgb',
        unreal.MaterialProperty.MP_BASE_COLOR
    )
    #Specular-操控属性
    scalarparam = unreal.MaterialEditingLibrary.create_material_expression(
        material,
        unreal.MaterialExpressionScalarParameter,
        -200,
        200
    )
    scalarparam.set_editor_property('parameter_name','Specular Level')
    unreal.MaterialEditingLibrary.connect_material_property(
        scalarparam,
        "",
        unreal.MaterialProperty.MP_SPECULAR
    )
    #AO-AO
    texturesample = unreal.MaterialEditingLibrary.create_material_expression(
        material,
        unreal.MaterialExpressionTextureSampleParameter2D,
        -200.0,
        400.0
    )
    texturesample.set_editor_property("parameter_name", "AO Rough Mtl Textures")
    texturesample.sampler_type = unreal.MaterialSamplerType.SAMPLERTYPE_LINEAR_COLOR
    unreal.MaterialEditingLibrary.connect_material_property(texturesample, "r",
                                                            unreal.MaterialProperty.MP_AMBIENT_OCCLUSION)
    unreal.MaterialEditingLibrary.connect_material_property(texturesample, "g", unreal.MaterialProperty.MP_ROUGHNESS)
    unreal.MaterialEditingLibrary.connect_material_property(texturesample, "b", unreal.MaterialProperty.MP_METALLIC)

    #Normal -法线
    texturesample = unreal.MaterialEditingLibrary.create_material_expression(
        material,
        unreal.MaterialExpressionTextureSampleParameter2D,
        -200.0,
        600.0
    )
    texturesample.sampler_type = unreal.MaterialSamplerType.SAMPLERTYPE_NORMAL
    texturesample.set_editor_property("parameter_name", "Normal Texture")
    unreal.MaterialEditingLibrary.connect_material_property(texturesample, "rgb", unreal.MaterialProperty.MP_NORMAL)