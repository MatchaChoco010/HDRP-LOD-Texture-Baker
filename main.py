#!/usr/bin/env python
# -*- coding: utf8 -*-
import os
import sys
import subprocess
import threading
import re
from datetime import datetime
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
from pysbs import batchtools
from pysbs import context


if __name__ == "__main__":
    def button_hi_fbx_select_clicked():
        initialdir = ''
        filetype = [("fbx", "*.fbx")]
        filepath = filedialog.askopenfilename(
            filetypes=filetype, initialdir=initialdir)
        s_hi_fbx_path.set(filepath)

    def button_lod0_fbx_select_clicked():
        initialdir = ''
        filetype = [("fbx", "*.fbx")]
        filepath = filedialog.askopenfilename(
            filetypes=filetype, initialdir=initialdir)
        s_lod0_fbx_path.set(filepath)

    def button_lod0_basecolor_texture_select_ckicked():
        initialdir = ""
        filetype = [("tga", "*.tga"), ("png", "*.png")]
        filepath = filedialog.askopenfilename(
            filetype=filetype, initialdir=initialdir)
        s_lod0_basecolor_texture_path.set(filepath)

    def button_lod0_maskmap_texture_select_ckicked():
        initialdir = ""
        filetype = [("tga", "*.tga"), ("png", "*.png")]
        filepath = filedialog.askopenfilename(
            filetype=filetype, initialdir=initialdir)
        s_lod0_maskmap_texture_path.set(filepath)

    def button_lod0_normal_texture_select_ckicked():
        initialdir = ""
        filetype = [("tga", "*.tga"), ("png", "*.png")]
        filepath = filedialog.askopenfilename(
            filetype=filetype, initialdir=initialdir)
        s_lod0_normal_texture_path.set(filepath)

    def button_lod0_micronormal_texture_select_ckicked():
        initialdir = ""
        filetype = [("tga", "*.tga"), ("png", "*.png")]
        filepath = filedialog.askopenfilename(
            filetype=filetype, initialdir=initialdir)
        s_lod0_micronormal_texture_path.set(filepath)

    def button_lod0_height_texture_select_ckicked():
        initialdir = ""
        filetype = [("tga", "*.tga"), ("png", "*.png")]
        filepath = filedialog.askopenfilename(
            filetype=filetype, initialdir=initialdir)
        s_lod0_height_texture_path.set(filepath)

    def button_lod1_fbx_select_clicked():
        initialdir = ''
        filetype = [("fbx", "*.fbx")]
        filepath = filedialog.askopenfilename(
            filetypes=filetype, initialdir=initialdir)
        s_lod1_fbx_path.set(filepath)

    def button_lod2_fbx_select_clicked():
        initialdir = ''
        filetype = [("fbx", "*.fbx")]
        filepath = filedialog.askopenfilename(
            filetypes=filetype, initialdir=initialdir)
        s_lod2_fbx_path.set(filepath)

    def button_output_dir_select_clicked():
        initialdir = ''
        dirpath = filedialog.askdirectory(initialdir=initialdir)
        s_output_dir_path.set(dirpath)

    def validate_value_01(P):
        if P == "":
            return True
        else:
            try:
                value = float(P)
                if 0 <= value and value <= 1:
                    return True
                else:
                    return False
            except ValueError:
                return False

    def validate_output_size(P):
        if P == "":
            return True
        else:
            try:
                value = int(P)
                if 0 <= value and value <= 12:
                    return True
                else:
                    return False
            except ValueError:
                return False

    def message(text, error=False):
        t = ("[%s] " + text) % datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        if error:
            status_message_tree.insert("", tk.END, text=t, tags=("error", ))
        else:
            status_message_tree.insert("", tk.END, text=t)
        status_message_tree.yview_moveto(1)

    def release():
        button_execution.configure(state=tk.NORMAL)
        bake_lock.release()

    def bake():
        message("Bake start...")

        aContext = context.Context()

        progress = 0
        max_progress = 2
        status_progressbar.configure(value=progress)
        status_progressbar.configure(maximum=max_progress)

        # Get an Validate Inputs
        hi_fbx_path = entry_hi_fbx_path.get()
        if hi_fbx_path == "":
            message("Hi fbx model path is required.", error=True)
            release()
            return
        if not os.path.exists(hi_fbx_path):
            message("Hi fbx model does not exist.", error=True)
            release()
            return
        if not os.path.isfile(hi_fbx_path):
            message("Hi fbx model is not a file.", error=True)
            release()
            return
        message("Hi model path: %s" % hi_fbx_path)

        lod0_fbx_path = entry_lod0_fbx_path.get()
        if lod0_fbx_path == "":
            message("LOD0 fbx model path is required.", error=True)
            release()
            return
        if not os.path.exists(lod0_fbx_path):
            message("LOD0 fbx model does not exist.", error=True)
            release()
            return
        if not os.path.isfile(lod0_fbx_path):
            message("LOD0 fbx model is not a file.", error=True)
            release()
            return
        message("LOD0 model path: %s" % lod0_fbx_path)

        lod0_basecolor_texture_path = entry_lod0_basecolor_texture_path.get()
        if lod0_basecolor_texture_path == "":
            message("LOD0 BaseColor texture path is required.", error=True)
            release()
            return
        if not os.path.exists(lod0_basecolor_texture_path):
            message("LOD0 BaseColor texture does not exist.", error=True)
            release()
            return
        if not os.path.isfile(lod0_basecolor_texture_path):
            message("LOD0 BaseColor texture is not a file.", error=True)
            release()
            return
        message("LOD0 BaseColor texture path: %s" %
                lod0_basecolor_texture_path)

        lod0_maskmap_texture_path = entry_lod0_maskmap_texture_path.get()
        if lod0_maskmap_texture_path == "":
            message("LOD0 MaskMap texture path is required.", error=True)
            release()
            return
        if not os.path.exists(lod0_maskmap_texture_path):
            message("LOD0 MaskMap texture does not exist.", error=True)
            release()
            return
        if not os.path.isfile(lod0_maskmap_texture_path):
            message("LOD0 MaskMap texture is not a file.", error=True)
            release()
            return
        message("LOD0 MaskMap texture path: %s" % lod0_maskmap_texture_path)

        lod0_normal_texture_path = entry_lod0_normal_texture_path.get()
        if lod0_normal_texture_path == "":
            message("LOD0 Normal texture path is required.", error=True)
            release()
            return
        if not os.path.exists(lod0_normal_texture_path):
            message("LOD0 Normal texture does not exist.", error=True)
            release()
            return
        if not os.path.isfile(lod0_normal_texture_path):
            message("LOD0 Normal texture is not a file.", error=True)
            release()
            return
        message("LOD0 Normal texture path: %s" % lod0_normal_texture_path)

        lod0_micronormal_texture_path = \
            entry_lod0_micronormal_texture_path.get()
        if lod0_micronormal_texture_path == "":
            message("LOD0 MicroNormal texture is not provided.")
        if not lod0_micronormal_texture_path == "":
            if not os.path.exists(lod0_micronormal_texture_path):
                message("LOD0 MicroNormal texture does not exist.", error=True)
                release()
                return
            else:
                message("LOD0 MicroNormal texture path: %s" %
                        lod0_micronormal_texture_path)

        lod0_height_texture_path = entry_lod0_height_texture_path.get()
        if lod0_height_texture_path == "":
            message("LOD0 Height texture is not provided.")
        if not lod0_height_texture_path == "":
            if not os.path.exists(lod0_height_texture_path):
                message("LOD0 Height texture does not exist.", error=True)
                release()
                return
            else:
                message("LOD0 Height texture path: %s" %
                        lod0_height_texture_path)

        lod0_max_frontal = d_lod0_max_frontal.get()
        lod0_max_rear = d_lod0_max_rear.get()
        lod0_average_normals = b_lod0_average_normals.get()
        lod0_output_size = i_lod0_output_size.get()
        message("LOD0 max frontal: %s" % lod0_max_frontal)
        message("LOD0 max rear: %s" % lod0_max_rear)
        message("LOD0 average normals: %s" % lod0_average_normals)
        message("LOD0 output size: %s" % lod0_output_size)

        lod1_fbx_path = entry_lod1_fbx_path.get()
        lod1_max_frontal = d_lod1_max_frontal.get()
        lod1_max_rear = d_lod1_max_rear.get()
        lod1_average_normals = b_lod1_average_normals.get()
        lod1_output_size = i_lod1_output_size.get()
        if lod1_fbx_path == "":
            message("LOD1 fbx is not provided.")
        if not lod1_fbx_path == "":
            if not os.path.exists(lod1_fbx_path):
                message("LOD1 fbx does not exist.", error=True)
                release()
                return
            else:
                message("LOD1 fbx path: %s" % lod1_fbx_path)
                message("LOD1 max frontal: %s" % lod1_max_frontal)
                message("LOD1 max rear: %s" % lod1_max_rear)
                message("LOD1 average normals: %s" % lod1_average_normals)
                message("LOD1 output size: %s" % lod1_output_size)

        lod2_fbx_path = entry_lod2_fbx_path.get()
        lod2_max_frontal = d_lod2_max_frontal.get()
        lod2_max_rear = d_lod2_max_rear.get()
        lod2_average_normals = b_lod2_average_normals.get()
        lod2_output_size = i_lod2_output_size.get()
        if lod2_fbx_path == "":
            message("LOD2 fbx is not provided.")
        if not lod2_fbx_path == "":
            if not os.path.exists(lod2_fbx_path):
                message("LOD2 fbx does not exist.", error=True)
                release()
                return
            else:
                message("LOD2 fbx path: %s" % lod2_fbx_path)
                message("LOD2 max frontal: %s" % lod2_max_frontal)
                message("LOD2 max rear: %s" % lod2_max_rear)
                message("LOD2 average normals: %s" % lod2_average_normals)
                message("LOD2 output size: %s" % lod2_output_size)

        output_dir_path = entry_output_dir_path.get()
        if output_dir_path == "":
            message("Output Directory path is required.", error=True)
            release()
            return
        if not os.path.exists(output_dir_path):
            message("Output Directory does not exist.", error=True)
            release()
            return
        if not os.path.isdir(output_dir_path):
            message("Output Directory is not a directory.", error=True)
            release()
            return
        message("Output Directory path: %s" % output_dir_path)

        filename = s_output_filename.get()
        extension = os.path.splitext(filename)[1][1:]
        filename = os.path.splitext(filename)[0]
        if not extension in ["dds", "bmp", "jpg", "jif", "jpeg", "jpe", "png", "tga", "targa", "tif", "tiff", "wap", "wbmp", "wbm", "hdr", "exr", "webp", "psd"]:
            message("Output filname extension must be one of the following: dds, bmp, jpg, jif, jpeg, jpe, png, tga, targa, tif, tiff, wap, wbmp, wbm, hdr, exr, webp, psd", error=True)
            release()
            return
        message("Output format: %s" % extension)
        lod0_filename = re.sub(r"\{lod\}", "LOD0", filename)
        lod1_filename = re.sub(r"\{lod\}", "LOD1", filename)
        lod2_filename = re.sub(r"\{lod\}", "LOD2", filename)

        if not lod1_fbx_path == "" or not lod2_fbx_path == "":
            max_progress += 1
        if not lod1_fbx_path == "":
            max_progress += 10
            if not lod0_micronormal_texture_path == "":
                max_progress += 1
            if not lod0_height_texture_path == "":
                max_progress += 1
        if not lod2_fbx_path == "":
            max_progress += 10
            if not lod0_micronormal_texture_path == "":
                max_progress += 1
            if not lod0_height_texture_path == "":
                max_progress += 1
        status_progressbar.configure(maximum=max_progress)

        # Create Directories
        tmp_dir_path = os.path.join(output_dir_path, "tmp")
        os.makedirs(tmp_dir_path, exist_ok=True)
        lod0_dir_path = os.path.join(output_dir_path, "LOD0")
        os.makedirs(lod0_dir_path, exist_ok=True)
        if not lod1_fbx_path == "":
            lod1_dir_path = os.path.join(output_dir_path, "LOD1")
            os.makedirs(lod1_dir_path, exist_ok=True)
        if not lod2_fbx_path == "":
            lod2_dir_path = os.path.join(output_dir_path, "LOD2")
            os.makedirs(lod2_dir_path, exist_ok=True)

        # Template Path
        output_template_path = os.path.join(
            os.path.dirname(__file__), "output.sbs")
        split_maskmap_template_path = os.path.join(
            os.path.dirname(__file__), "split_maskmap.sbs")
        merge_maskmap_template_path = os.path.join(
            os.path.dirname(__file__), "merge_maskmap.sbs")
        combine_normal_template_path = os.path.join(
            os.path.dirname(__file__), "combine_normal.sbs")

# LOD0
        # Bake LOD0 BentNormal
        message("Start baking LOD0 BentNormal map...")
        lod0_bent_normal_filename = \
            re.sub(r"\{textureName\}", "BentNormal", lod0_filename)
        proc = batchtools.sbsbaker_bent_normal_from_mesh(
            lod0_fbx_path,
            highdef_mesh=hi_fbx_path,
            output_size=(lod0_output_size, lod0_output_size),
            output_name=lod0_bent_normal_filename,
            output_path=tmp_dir_path,
            output_format=extension,
            normal_format="0",
            max_frontal=lod0_max_frontal,
            max_rear=lod0_max_rear,
            average_normals=False,
            stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        (_, err) = proc.communicate()
        proc.wait()
        if err:
            message("%s" % err, error=True)
            status_progressbar.configure(value=0)
            return
        progress += 1
        status_progressbar.configure(value=progress)
        message("Finish baking LOD0 BentNormal map.")

        # Render LOD0 Output
        message("Start render LOD0 output textures...")
        connect_image = [
            "input_basecolor@path@" + lod0_basecolor_texture_path,
            "input_maskmap@path@" + lod0_maskmap_texture_path,
            "input_normal@path@" + lod0_normal_texture_path,
            "input_bentnormal@path@" +
            os.path.join(
                tmp_dir_path, lod0_bent_normal_filename + "." + extension)
        ]
        proc = batchtools.sbsmutator_edit(
            input=output_template_path,
            presets_path=aContext.getDefaultPackagePath(),
            output_name="LOD0_output",
            output_path=tmp_dir_path,
            instantiate=True,
            connect_image=connect_image,
            stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        (_, err) = proc.communicate()
        proc.wait()
        if err:
            message(err, error=True)
            status_progressbar.configure(value=0)
            return
        message("Created specialized LOD0_output.sbs.")
        proc = batchtools.sbscooker(
            inputs=os.path.join(tmp_dir_path, "LOD0_output") + ".sbs",
            includes=aContext.getDefaultPackagePath(),
            size_limit=12,
            output_path=tmp_dir_path,
            stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        (_, err) = proc.communicate()
        proc.wait()
        if err:
            message(err, error=True)
            status_progressbar.configure(value=0)
            return
        message("Created LOD0_output.sbsar.")
        proc = batchtools.sbsrender_render(
            inputs=os.path.join(tmp_dir_path, "LOD0_output") + ".sbsar",
            output_name=re.sub(r"\{textureName\}",
                               "{outputNodeName}", lod0_filename),
            output_path=lod0_dir_path,
            output_format=extension,
            set_value=("$outputsize@%s,%s" %
                       (lod0_output_size, lod0_output_size)),
            stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        (_, err) = proc.communicate()
        proc.wait()
        if err:
            message(err, error=True)
            status_progressbar.configure(value=0)
            return
        progress += 1
        status_progressbar.configure(value=progress)
        message("Finish render LOD0 output textures.")

        if not lod1_fbx_path == "" or not lod2_fbx_path == "":

            # Split MaskMap
            message("Start splitting Lod0 MaskMap...")
            connect_image = [
                "input_maskmap@path@" + lod0_maskmap_texture_path,
            ]
            proc = batchtools.sbsmutator_edit(
                input=split_maskmap_template_path,
                presets_path=aContext.getDefaultPackagePath(),
                output_name="LOD0_split_maskmap",
                output_path=tmp_dir_path,
                instantiate=True,
                connect_image=connect_image,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message(err, error=True)
                status_progressbar.configure(value=0)
                return
            message("Created specialized LOD0_split_maskmap.sbs.")
            proc = batchtools.sbscooker(
                inputs=os.path.join(
                    tmp_dir_path, "LOD0_split_maskmap") + ".sbs",
                includes=aContext.getDefaultPackagePath(),
                size_limit=12,
                output_path=tmp_dir_path,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message(err, error=True)
                status_progressbar.configure(value=0)
                return
            message("Created LOD0_split_maskmap.sbsar.")
            proc = batchtools.sbsrender_render(
                inputs=os.path.join(
                    tmp_dir_path, "LOD0_split_maskmap") + ".sbsar",
                output_name=re.sub(r"\{textureName\}",
                                   "{outputNodeName}", lod0_filename),
                output_path=tmp_dir_path,
                output_format=extension,
                set_value=("$outputsize@%s,%s" %
                           (lod0_output_size, lod0_output_size)),
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message(err, error=True)
                status_progressbar.configure(value=0)
                return
            progress += 1
            status_progressbar.configure(value=progress)
            message("Finish splitting LOD0 MaskMap.")

# LOD1
        if not lod1_fbx_path == "":

            message("Start baking LOD1 textures.")

            # Bake LOD1 AmbientOcclusion
            message("Start baking LOD1 AmbientOcclusion map...")
            lod1_ambient_occlusion_filename = \
                re.sub(r"\{textureName\}", "AmbientOcclusion", lod1_filename)
            proc = batchtools.sbsbaker_ambient_occlusion_from_mesh(
                lod1_fbx_path,
                highdef_mesh=hi_fbx_path,
                output_size=(lod1_output_size, lod1_output_size),
                output_name=lod1_ambient_occlusion_filename,
                output_path=tmp_dir_path,
                output_format=extension,
                normal_format="0",
                max_frontal=lod1_max_frontal,
                max_rear=lod1_max_rear,
                average_normals=False,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message("%s" % err, error=True)
                status_progressbar.configure(value=0)
                return
            progress += 1
            status_progressbar.configure(value=progress)
            message("Finish baking LOD1 AmbientOcclusion map.")

            # Bake LOD1 BentNormal
            message("Start baking LOD1 BentNormal map...")
            lod1_bent_normal_filename = \
                re.sub(r"\{textureName\}", "BentNormal", lod1_filename)
            proc = batchtools.sbsbaker_bent_normal_from_mesh(
                lod1_fbx_path,
                highdef_mesh=hi_fbx_path,
                output_size=(lod1_output_size, lod1_output_size),
                output_name=lod1_bent_normal_filename,
                output_path=tmp_dir_path,
                output_format=extension,
                normal_format="0",
                max_frontal=lod1_max_frontal,
                max_rear=lod1_max_rear,
                average_normals=False,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message("%s" % err, error=True)
                status_progressbar.configure(value=0)
                return
            progress += 1
            status_progressbar.configure(value=progress)
            message("Finish baking LOD1 BentNormal map.")

            # Bake LOD1 Normal
            message("Start baking LOD1 Normal map...")
            lod1_normal_filename = \
                re.sub(r"\{textureName\}", "NormalFromMesh", lod1_filename)
            proc = batchtools.sbsbaker_normal_from_mesh(
                lod1_fbx_path,
                highdef_mesh=hi_fbx_path,
                output_size=(lod1_output_size, lod1_output_size),
                output_name=lod1_normal_filename,
                output_path=tmp_dir_path,
                output_format=extension,
                normal_format="0",
                max_frontal=lod1_max_frontal,
                max_rear=lod1_max_rear,
                average_normals=False,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message("%s" % err, error=True)
                status_progressbar.configure(value=0)
                return
            progress += 1
            status_progressbar.configure(value=progress)
            message("Finish baking LOD1 Normal map.")

            # Transfer LOD0 BaseColor to LOD1
            message("Start transferring LOD0 BaseColor to LOD1...")
            lod1_basecolor_filename = \
                re.sub(r"\{textureName\}", "BaseColor", lod1_filename)
            proc = batchtools.sbsbaker_texture_from_mesh(
                lod1_fbx_path,
                highdef_mesh=lod0_fbx_path,
                texture_file=lod0_basecolor_texture_path,
                output_size=(lod1_output_size, lod1_output_size),
                output_name=lod1_basecolor_filename,
                output_path=tmp_dir_path,
                output_format=extension,
                normal_format="0",
                normal_map=False,
                max_frontal=lod1_max_frontal,
                max_rear=lod1_max_rear,
                average_normals=False,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message("%s" % err, error=True)
                status_progressbar.configure(value=0)
                return
            progress += 1
            status_progressbar.configure(value=progress)
            message("Finish transferring LOD0 BaseColor to LOD1.")

            # Transfer LOD0 Metallic to LOD1
            message("Start transferring LOD0 Metallic to LOD1...")
            lod1_metallic_filename = \
                re.sub(r"\{textureName\}", "Metallic", lod1_filename)
            proc = batchtools.sbsbaker_texture_from_mesh(
                lod1_fbx_path,
                highdef_mesh=lod0_fbx_path,
                texture_file=os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "Metallic",
                           lod0_filename)) + "." + extension,
                output_size=(lod1_output_size, lod1_output_size),
                output_name=lod1_metallic_filename,
                output_path=tmp_dir_path,
                output_format=extension,
                normal_format="0",
                normal_map=False,
                max_frontal=lod1_max_frontal,
                max_rear=lod1_max_rear,
                average_normals=False,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message("%s" % err, error=True)
                status_progressbar.configure(value=0)
                return
            progress += 1
            status_progressbar.configure(value=progress)
            message("Finish transferring LOD0 Metallic to LOD1.")

            # Transfer LOD0 Smoothness to LOD1
            message("Start transferring LOD0 Smoothness to LOD1...")
            lod1_smoothness_filename = \
                re.sub(r"\{textureName\}", "Smoothness", lod1_filename)
            proc = batchtools.sbsbaker_texture_from_mesh(
                lod1_fbx_path,
                highdef_mesh=lod0_fbx_path,
                texture_file=os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "Smoothness",
                           lod0_filename)) + "." + extension,
                output_size=(lod1_output_size, lod1_output_size),
                output_name=lod1_smoothness_filename,
                output_path=tmp_dir_path,
                output_format=extension,
                normal_format="0",
                normal_map=False,
                max_frontal=lod1_max_frontal,
                max_rear=lod1_max_rear,
                average_normals=False,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message("%s" % err, error=True)
                status_progressbar.configure(value=0)
                return
            progress += 1
            status_progressbar.configure(value=progress)
            message("Finish transferring LOD0 Smoothness to LOD1.")

            # Transfer LOD0 DetailMask to LOD1
            message("Start transferring LOD0 DetailMask to LOD1...")
            lod1_detailmask_filename = \
                re.sub(r"\{textureName\}", "DetailMask", lod1_filename)
            proc = batchtools.sbsbaker_texture_from_mesh(
                lod1_fbx_path,
                highdef_mesh=lod0_fbx_path,
                texture_file=os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "DetailMask",
                           lod0_filename)) + "." + extension,
                output_size=(lod1_output_size, lod1_output_size),
                output_name=lod1_detailmask_filename,
                output_path=tmp_dir_path,
                output_format=extension,
                normal_format="0",
                normal_map=False,
                max_frontal=lod1_max_frontal,
                max_rear=lod1_max_rear,
                average_normals=False,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message("%s" % err, error=True)
                status_progressbar.configure(value=0)
                return
            progress += 1
            status_progressbar.configure(value=progress)
            message("Finish transferring LOD0 DetailMask to LOD1.")

            if not lod0_micronormal_texture_path == "":
                # Transfer LOD0 MicroNormal to LOD1
                message("Start transferring LOD0 MicroNormal to LOD1...")
                lod1_micronormal_filename = \
                    re.sub(r"\{textureName\}", "MicroNormal", lod1_filename)
                proc = batchtools.sbsbaker_texture_from_mesh(
                    lod1_fbx_path,
                    highdef_mesh=lod0_fbx_path,
                    texture_file=lod0_micronormal_texture_path,
                    output_size=(lod1_output_size, lod1_output_size),
                    output_name=lod1_micronormal_filename,
                    output_path=tmp_dir_path,
                    output_format=extension,
                    normal_format="0",
                    normal_map=True,
                    max_frontal=lod1_max_frontal,
                    max_rear=lod1_max_rear,
                    average_normals=False,
                    stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                (_, err) = proc.communicate()
                proc.wait()
                if err:
                    message("%s" % err, error=True)
                    status_progressbar.configure(value=0)
                    return
                progress += 1
                status_progressbar.configure(value=progress)
                message("Finish transferring LOD0 MicroNormal to LOD1.")

            if not lod0_height_texture_path == "":
                # Transfer LOD0 Height to LOD1
                message("Start transferring LOD0 Height to LOD1...")
                lod1_height_filename = \
                    re.sub(r"\{textureName\}", "Height", lod1_filename)
                proc = batchtools.sbsbaker_texture_from_mesh(
                    lod1_fbx_path,
                    highdef_mesh=lod0_fbx_path,
                    texture_file=lod0_height_texture_path,
                    output_size=(lod1_output_size, lod1_output_size),
                    output_name=lod1_height_filename,
                    output_path=tmp_dir_path,
                    output_format=extension,
                    normal_format="0",
                    normal_map=False,
                    max_frontal=lod1_max_frontal,
                    max_rear=lod1_max_rear,
                    average_normals=False,
                    stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                (_, err) = proc.communicate()
                proc.wait()
                if err:
                    message("%s" % err, error=True)
                    status_progressbar.configure(value=0)
                    return
                progress += 1
                status_progressbar.configure(value=progress)
                message("Finish transferring LOD0 Height to LOD1.")

            # Merge LOD1 MaskMap
            message("Start merging Lod1 MaskMap...")
            connect_image = [
                "input_metallic@path@" + os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "Metallic",
                           lod1_filename) + "." + extension
                ),
                "input_ambientocclusion@path@" + os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "AmbientOCclusion",
                           lod1_filename) + "." + extension
                ),
                "input_detailmask@path@" + os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "DetailMask",
                           lod1_filename) + "." + extension
                ),
                "input_smoothness@path@" + os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "Smoothness",
                           lod1_filename) + "." + extension
                ),
            ]
            proc = batchtools.sbsmutator_edit(
                input=merge_maskmap_template_path,
                presets_path=aContext.getDefaultPackagePath(),
                output_name="LOD1_merge_maskmap",
                output_path=tmp_dir_path,
                instantiate=True,
                connect_image=connect_image,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message(err, error=True)
                status_progressbar.configure(value=0)
                return
            message("Created specialized LOD1_merge_maskmap.sbs.")
            proc = batchtools.sbscooker(
                inputs=os.path.join(
                    tmp_dir_path, "LOD1_merge_maskmap") + ".sbs",
                includes=aContext.getDefaultPackagePath(),
                size_limit=12,
                output_path=tmp_dir_path,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message(err, error=True)
                status_progressbar.configure(value=0)
                return
            message("Created LOD1_merge_maskmap.sbsar.")
            proc = batchtools.sbsrender_render(
                inputs=os.path.join(
                    tmp_dir_path, "LOD1_merge_maskmap") + ".sbsar",
                output_name=re.sub(r"\{textureName\}",
                                   "{outputNodeName}", lod1_filename),
                output_path=tmp_dir_path,
                output_format=extension,
                set_value=("$outputsize@%s,%s" %
                           (lod1_output_size, lod1_output_size)),
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message(err, error=True)
                status_progressbar.configure(value=0)
                return
            progress += 1
            status_progressbar.configure(value=progress)
            message("Finish merging LOD1 MaskMap.")

            # Combine Lod1 Normal
            message("Start combining Lod1 Normal...")
            connect_image = [
                "input_height@path@" + os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "Height",
                           lod1_filename) + "." + extension
                ),
                "input_micronormal@path@" + os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "MicroNormal",
                           lod1_filename) + "." + extension
                ),
                "input_normalfrommesh@path@" + os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "NormalFromMesh",
                           lod1_filename) + "." + extension
                )
            ]
            proc = batchtools.sbsmutator_edit(
                input=combine_normal_template_path,
                presets_path=aContext.getDefaultPackagePath(),
                output_name="LOD1_combine_normal",
                output_path=tmp_dir_path,
                instantiate=True,
                connect_image=connect_image,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message(err, error=True)
                status_progressbar.configure(value=0)
                return
            message("Created specialized LOD1_combine_normal.sbs.")
            proc = batchtools.sbscooker(
                inputs=os.path.join(
                    tmp_dir_path, "LOD1_combine_normal") + ".sbs",
                includes=aContext.getDefaultPackagePath(),
                size_limit=12,
                output_path=tmp_dir_path,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message(err, error=True)
                status_progressbar.configure(value=0)
                return
            message("Created LOD1_combine_normal.sbsar.")
            proc = batchtools.sbsrender_render(
                inputs=os.path.join(
                    tmp_dir_path, "LOD1_combine_normal") + ".sbsar",
                output_name=re.sub(r"\{textureName\}",
                                   "{outputNodeName}", lod1_filename),
                output_path=tmp_dir_path,
                output_format=extension,
                set_value=("$outputsize@%s,%s" %
                           (lod1_output_size, lod1_output_size)),
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message(err, error=True)
                status_progressbar.configure(value=0)
                return
            progress += 1
            status_progressbar.configure(value=progress)
            message("Finish merging LOD1 MaskMap.")

            # Render LOD1 Output
            message("Start render LOD1 output textures...")
            connect_image = [
                "input_basecolor@path@" + os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "BaseColor",
                           lod1_filename) + "." + extension
                ),
                "input_maskmap@path@" + os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "MaskMap",
                           lod1_filename) + "." + extension
                ),
                "input_normal@path@" + os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "Normal",
                           lod1_filename) + "." + extension
                ),
                "input_bentnormal@path@" + os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "BentNormal",
                           lod1_filename) + "." + extension
                ),
            ]
            proc = batchtools.sbsmutator_edit(
                input=output_template_path,
                presets_path=aContext.getDefaultPackagePath(),
                output_name="LOD1_output",
                output_path=tmp_dir_path,
                instantiate=True,
                connect_image=connect_image,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message(err, error=True)
                status_progressbar.configure(value=0)
                return
            message("Created specialized LOD1_output.sbs.")
            proc = batchtools.sbscooker(
                inputs=os.path.join(tmp_dir_path, "LOD1_output") + ".sbs",
                includes=aContext.getDefaultPackagePath(),
                size_limit=12,
                output_path=tmp_dir_path,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message(err, error=True)
                status_progressbar.configure(value=0)
                return
            message("Created LOD1_output.sbsar.")
            proc = batchtools.sbsrender_render(
                inputs=os.path.join(tmp_dir_path, "LOD1_output") + ".sbsar",
                output_name=re.sub(r"\{textureName\}",
                                   "{outputNodeName}", lod1_filename),
                output_path=lod1_dir_path,
                output_format=extension,
                set_value=("$outputsize@%s,%s" %
                           (lod1_output_size, lod1_output_size)),
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message(err, error=True)
                status_progressbar.configure(value=0)
                return
            progress += 1
            status_progressbar.configure(value=progress)
            message("Finish render LOD1 output textures.")

            message("Finish baking LOD1 textures.")

# LOD2
        if not lod2_fbx_path == "":

            message("Start baking LOD2 textures.")

            # Bake LOD2 AmbientOcclusion
            message("Start baking LOD2 AmbientOcclusion map...")
            lod2_ambient_occlusion_filename = \
                re.sub(r"\{textureName\}", "AmbientOcclusion", lod2_filename)
            proc = batchtools.sbsbaker_ambient_occlusion_from_mesh(
                lod2_fbx_path,
                highdef_mesh=hi_fbx_path,
                output_size=(lod2_output_size, lod2_output_size),
                output_name=lod2_ambient_occlusion_filename,
                output_path=tmp_dir_path,
                output_format=extension,
                normal_format="0",
                max_frontal=lod2_max_frontal,
                max_rear=lod2_max_rear,
                average_normals=False,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message("%s" % err, error=True)
                status_progressbar.configure(value=0)
                return
            progress += 1
            status_progressbar.configure(value=progress)
            message("Finish baking LOD2 AmbientOcclusion map.")

            # Bake LOD2 BentNormal
            message("Start baking LOD2 BentNormal map...")
            lod2_bent_normal_filename = \
                re.sub(r"\{textureName\}", "BentNormal", lod2_filename)
            proc = batchtools.sbsbaker_bent_normal_from_mesh(
                lod2_fbx_path,
                highdef_mesh=hi_fbx_path,
                output_size=(lod2_output_size, lod2_output_size),
                output_name=lod2_bent_normal_filename,
                output_path=tmp_dir_path,
                output_format=extension,
                normal_format="0",
                max_frontal=lod2_max_frontal,
                max_rear=lod2_max_rear,
                average_normals=False,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message("%s" % err, error=True)
                status_progressbar.configure(value=0)
                return
            progress += 1
            status_progressbar.configure(value=progress)
            message("Finish baking LOD2 BentNormal map.")

            # Bake LOD2 Normal
            message("Start baking LOD2 Normal map...")
            lod2_normal_filename = \
                re.sub(r"\{textureName\}", "NormalFromMesh", lod2_filename)
            proc = batchtools.sbsbaker_normal_from_mesh(
                lod2_fbx_path,
                highdef_mesh=hi_fbx_path,
                output_size=(lod2_output_size, lod2_output_size),
                output_name=lod2_normal_filename,
                output_path=tmp_dir_path,
                output_format=extension,
                normal_format="0",
                max_frontal=lod2_max_frontal,
                max_rear=lod2_max_rear,
                average_normals=False,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message("%s" % err, error=True)
                status_progressbar.configure(value=0)
                return
            progress += 1
            status_progressbar.configure(value=progress)
            message("Finish baking LOD2 Normal map.")

            # Transfer LOD0 BaseColor to LOD2
            message("Start transferring LOD0 BaseColor to LOD2...")
            lod2_basecolor_filename = \
                re.sub(r"\{textureName\}", "BaseColor", lod2_filename)
            proc = batchtools.sbsbaker_texture_from_mesh(
                lod2_fbx_path,
                highdef_mesh=lod0_fbx_path,
                texture_file=lod0_basecolor_texture_path,
                output_size=(lod2_output_size, lod2_output_size),
                output_name=lod2_basecolor_filename,
                output_path=tmp_dir_path,
                output_format=extension,
                normal_format="0",
                normal_map=False,
                max_frontal=lod2_max_frontal,
                max_rear=lod2_max_rear,
                average_normals=False,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message("%s" % err, error=True)
                status_progressbar.configure(value=0)
                return
            progress += 1
            status_progressbar.configure(value=progress)
            message("Finish transferring LOD0 BaseColor to LOD2.")

            # Transfer LOD0 Metallic to LOD2
            message("Start transferring LOD0 Metallic to LOD2...")
            lod2_metallic_filename = \
                re.sub(r"\{textureName\}", "Metallic", lod2_filename)
            proc = batchtools.sbsbaker_texture_from_mesh(
                lod2_fbx_path,
                highdef_mesh=lod0_fbx_path,
                texture_file=os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "Metallic",
                           lod0_filename)) + "." + extension,
                output_size=(lod2_output_size, lod2_output_size),
                output_name=lod2_metallic_filename,
                output_path=tmp_dir_path,
                output_format=extension,
                normal_format="0",
                normal_map=False,
                max_frontal=lod2_max_frontal,
                max_rear=lod2_max_rear,
                average_normals=False,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message("%s" % err, error=True)
                status_progressbar.configure(value=0)
                return
            progress += 1
            status_progressbar.configure(value=progress)
            message("Finish transferring LOD0 Metallic to LOD2.")

            # Transfer LOD0 Smoothness to LOD2
            message("Start transferring LOD0 Smoothness to LOD2...")
            lod2_smoothness_filename = \
                re.sub(r"\{textureName\}", "Smoothness", lod2_filename)
            proc = batchtools.sbsbaker_texture_from_mesh(
                lod2_fbx_path,
                highdef_mesh=lod0_fbx_path,
                texture_file=os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "Smoothness",
                           lod0_filename)) + "." + extension,
                output_size=(lod2_output_size, lod2_output_size),
                output_name=lod2_smoothness_filename,
                output_path=tmp_dir_path,
                output_format=extension,
                normal_format="0",
                normal_map=False,
                max_frontal=lod2_max_frontal,
                max_rear=lod2_max_rear,
                average_normals=False,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message("%s" % err, error=True)
                status_progressbar.configure(value=0)
                return
            progress += 1
            status_progressbar.configure(value=progress)
            message("Finish transferring LOD0 Smoothness to LOD2.")

            # Transfer LOD0 DetailMask to LOD2
            message("Start transferring LOD0 DetailMask to LOD2...")
            lod2_detailmask_filename = \
                re.sub(r"\{textureName\}", "DetailMask", lod2_filename)
            proc = batchtools.sbsbaker_texture_from_mesh(
                lod2_fbx_path,
                highdef_mesh=lod0_fbx_path,
                texture_file=os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "DetailMask",
                           lod0_filename)) + "." + extension,
                output_size=(lod2_output_size, lod2_output_size),
                output_name=lod2_detailmask_filename,
                output_path=tmp_dir_path,
                output_format=extension,
                normal_format="0",
                normal_map=False,
                max_frontal=lod2_max_frontal,
                max_rear=lod2_max_rear,
                average_normals=False,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message("%s" % err, error=True)
                status_progressbar.configure(value=0)
                return
            progress += 1
            status_progressbar.configure(value=progress)
            message("Finish transferring LOD0 DetailMask to LOD2.")

            if not lod0_micronormal_texture_path == "":
                # Transfer LOD0 MicroNormal to LOD2
                message("Start transferring LOD0 MicroNormal to LOD2...")
                lod2_micronormal_filename = \
                    re.sub(r"\{textureName\}", "MicroNormal", lod2_filename)
                proc = batchtools.sbsbaker_texture_from_mesh(
                    lod2_fbx_path,
                    highdef_mesh=lod0_fbx_path,
                    texture_file=lod0_micronormal_texture_path,
                    output_size=(lod2_output_size, lod2_output_size),
                    output_name=lod2_micronormal_filename,
                    output_path=tmp_dir_path,
                    output_format=extension,
                    normal_format="0",
                    normal_map=True,
                    max_frontal=lod2_max_frontal,
                    max_rear=lod2_max_rear,
                    average_normals=False,
                    stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                (_, err) = proc.communicate()
                proc.wait()
                if err:
                    message("%s" % err, error=True)
                    status_progressbar.configure(value=0)
                    return
                progress += 1
                status_progressbar.configure(value=progress)
                message("Finish transferring LOD0 MicroNormal to LOD2.")

            if not lod0_height_texture_path == "":
                # Transfer LOD0 Height to LOD2
                message("Start transferring LOD0 Height to LOD2...")
                lod2_height_filename = \
                    re.sub(r"\{textureName\}", "Height", lod2_filename)
                proc = batchtools.sbsbaker_texture_from_mesh(
                    lod2_fbx_path,
                    highdef_mesh=lod0_fbx_path,
                    texture_file=lod0_height_texture_path,
                    output_size=(lod2_output_size, lod2_output_size),
                    output_name=lod2_height_filename,
                    output_path=tmp_dir_path,
                    output_format=extension,
                    normal_format="0",
                    normal_map=False,
                    max_frontal=lod2_max_frontal,
                    max_rear=lod2_max_rear,
                    average_normals=False,
                    stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                (_, err) = proc.communicate()
                proc.wait()
                if err:
                    message("%s" % err, error=True)
                    status_progressbar.configure(value=0)
                    return
                progress += 1
                status_progressbar.configure(value=progress)
                message("Finish transferring LOD0 Height to LOD2.")

            # Merge LOD2 MaskMap
            message("Start merging Lod2 MaskMap...")
            connect_image = [
                "input_metallic@path@" + os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "Metallic",
                           lod2_filename) + "." + extension
                ),
                "input_ambientocclusion@path@" + os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "AmbientOCclusion",
                           lod2_filename) + "." + extension
                ),
                "input_detailmask@path@" + os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "DetailMask",
                           lod2_filename) + "." + extension
                ),
                "input_smoothness@path@" + os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "Smoothness",
                           lod2_filename) + "." + extension
                ),
            ]
            proc = batchtools.sbsmutator_edit(
                input=merge_maskmap_template_path,
                presets_path=aContext.getDefaultPackagePath(),
                output_name="LOD2_merge_maskmap",
                output_path=tmp_dir_path,
                instantiate=True,
                connect_image=connect_image,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message(err, error=True)
                status_progressbar.configure(value=0)
                return
            message("Created specialized LOD2_merge_maskmap.sbs.")
            proc = batchtools.sbscooker(
                inputs=os.path.join(
                    tmp_dir_path, "LOD2_merge_maskmap") + ".sbs",
                includes=aContext.getDefaultPackagePath(),
                size_limit=12,
                output_path=tmp_dir_path,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message(err, error=True)
                status_progressbar.configure(value=0)
                return
            message("Created LOD2_merge_maskmap.sbsar.")
            proc = batchtools.sbsrender_render(
                inputs=os.path.join(
                    tmp_dir_path, "LOD2_merge_maskmap") + ".sbsar",
                output_name=re.sub(r"\{textureName\}",
                                   "{outputNodeName}", lod2_filename),
                output_path=tmp_dir_path,
                output_format=extension,
                set_value=("$outputsize@%s,%s" %
                           (lod2_output_size, lod2_output_size)),
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message(err, error=True)
                status_progressbar.configure(value=0)
                return
            progress += 1
            status_progressbar.configure(value=progress)
            message("Finish merging LOD2 MaskMap.")

            # Combine Lod2 Normal
            message("Start combining Lod2 Normal...")
            connect_image = [
                "input_height@path@" + os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "Height",
                           lod2_filename) + "." + extension
                ),
                "input_micronormal@path@" + os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "MicroNormal",
                           lod2_filename) + "." + extension
                ),
                "input_normalfrommesh@path@" + os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "NormalFromMesh",
                           lod2_filename) + "." + extension
                )
            ]
            proc = batchtools.sbsmutator_edit(
                input=combine_normal_template_path,
                presets_path=aContext.getDefaultPackagePath(),
                output_name="LOD2_combine_normal",
                output_path=tmp_dir_path,
                instantiate=True,
                connect_image=connect_image,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message(err, error=True)
                status_progressbar.configure(value=0)
                return
            message("Created specialized LOD2_combine_normal.sbs.")
            proc = batchtools.sbscooker(
                inputs=os.path.join(
                    tmp_dir_path, "LOD2_combine_normal") + ".sbs",
                includes=aContext.getDefaultPackagePath(),
                size_limit=12,
                output_path=tmp_dir_path,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message(err, error=True)
                status_progressbar.configure(value=0)
                return
            message("Created LOD2_combine_normal.sbsar.")
            proc = batchtools.sbsrender_render(
                inputs=os.path.join(
                    tmp_dir_path, "LOD2_combine_normal") + ".sbsar",
                output_name=re.sub(r"\{textureName\}",
                                   "{outputNodeName}", lod2_filename),
                output_path=tmp_dir_path,
                output_format=extension,
                set_value=("$outputsize@%s,%s" %
                           (lod2_output_size, lod2_output_size)),
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message(err, error=True)
                status_progressbar.configure(value=0)
                return
            progress += 1
            status_progressbar.configure(value=progress)
            message("Finish merging LOD2 MaskMap.")

            # Render LOD2 Output
            message("Start render LOD2 output textures...")
            connect_image = [
                "input_basecolor@path@" + os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "BaseColor",
                           lod2_filename) + "." + extension
                ),
                "input_maskmap@path@" + os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "MaskMap",
                           lod2_filename) + "." + extension
                ),
                "input_normal@path@" + os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "Normal",
                           lod2_filename) + "." + extension
                ),
                "input_bentnormal@path@" + os.path.join(
                    tmp_dir_path,
                    re.sub(r"\{textureName\}", "BentNormal",
                           lod2_filename) + "." + extension
                ),
            ]
            proc = batchtools.sbsmutator_edit(
                input=output_template_path,
                presets_path=aContext.getDefaultPackagePath(),
                output_name="LOD2_output",
                output_path=tmp_dir_path,
                instantiate=True,
                connect_image=connect_image,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message(err, error=True)
                status_progressbar.configure(value=0)
                return
            message("Created specialized LOD2_output.sbs.")
            proc = batchtools.sbscooker(
                inputs=os.path.join(tmp_dir_path, "LOD2_output") + ".sbs",
                includes=aContext.getDefaultPackagePath(),
                size_limit=12,
                output_path=tmp_dir_path,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message(err, error=True)
                status_progressbar.configure(value=0)
                return
            message("Created LOD2_output.sbsar.")
            proc = batchtools.sbsrender_render(
                inputs=os.path.join(tmp_dir_path, "LOD2_output") + ".sbsar",
                output_name=re.sub(r"\{textureName\}",
                                   "{outputNodeName}", lod2_filename),
                output_path=lod2_dir_path,
                output_format=extension,
                set_value=("$outputsize@%s,%s" %
                           (lod2_output_size, lod2_output_size)),
                stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            (_, err) = proc.communicate()
            proc.wait()
            if err:
                message(err, error=True)
                status_progressbar.configure(value=0)
                return
            progress += 1
            status_progressbar.configure(value=progress)
            message("Finish render LOD2 output textures.")

            message("Finish baking LOD2 textures.")

        release()

    def bake_button_clicked():
        if bake_lock.acquire(blocking=False):
            button_execution.configure(state=tk.DISABLED)
            th = threading.Thread(target=bake)
            th.start()
        else:
            print(u"Already baking")

    #
    bake_lock = threading.Lock()
    root = tk.Tk()
    root.title('HDRP LOD Texture Baker')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    frame = ttk.Frame(root)
    frame.grid()

    # Hi
    label_hi = ttk.Label(
        frame, text="Hi",
        font=("", 0, "bold"),
        padding=(5, 2, 5, 2))
    label_hi.grid(row=1, column=1, sticky=(tk.S, tk.E))

    label_hi_fbx = ttk.Label(frame, text="* fbx", padding=(5, 2, 2, 2))
    label_hi_fbx.grid(row=1, column=2, sticky=(tk.S, tk.E))

    s_hi_fbx_path = tk.StringVar()
    entry_hi_fbx_path = ttk.Entry(frame, textvariable=s_hi_fbx_path, width=50)
    entry_hi_fbx_path.grid(row=1, column=3, sticky=tk.S, pady=2, padx=2)

    button_hi_fbx = ttk.Button(
        frame, text=u"参照", command=button_hi_fbx_select_clicked)
    button_hi_fbx.grid(row=1, column=4, sticky=tk.S)

    # LOD0
    label_lod0 = ttk.Label(
        frame, text="LOD0",
        font=("", 0, "bold"),
        padding=(5, 10, 2, 2))
    label_lod0.grid(row=3, column=1, sticky=(tk.S, tk.E))

    label_lod0_fbx = ttk.Label(frame, text="* fbx", padding=(5, 2, 2, 2))
    label_lod0_fbx.grid(row=3, column=2, sticky=(tk.S, tk.E))
    s_lod0_fbx_path = tk.StringVar()
    entry_lod0_fbx_path = ttk.Entry(
        frame, textvariable=s_lod0_fbx_path, width=50)
    entry_lod0_fbx_path.grid(row=3, column=3, sticky=tk.S, pady=2, padx=2)
    button_lod0_fbx = ttk.Button(
        frame, text=u"参照", command=button_lod0_fbx_select_clicked)
    button_lod0_fbx.grid(row=3, column=4, sticky=tk.S)

    label_lod0_basecolor_texture = ttk.Label(
        frame, text="* BaseColor texture", padding=(5, 2, 2, 2))
    label_lod0_basecolor_texture.grid(row=4, column=2, sticky=(tk.E, tk.S))
    s_lod0_basecolor_texture_path = tk.StringVar()
    entry_lod0_basecolor_texture_path = ttk.Entry(
        frame, textvariable=s_lod0_basecolor_texture_path, width=50)
    entry_lod0_basecolor_texture_path.grid(
        row=4, column=3, sticky=tk.S, pady=2, padx=2)
    button_lod0_basecolor_texture = ttk.Button(
        frame, text=u"参照",
        command=button_lod0_basecolor_texture_select_ckicked)
    button_lod0_basecolor_texture.grid(row=4, column=4, sticky=tk.S)

    label_lod0_maskmap_texture = ttk.Label(
        frame, text="* MaskMap texture", padding=(5, 2, 2, 2))
    label_lod0_maskmap_texture.grid(row=5, column=2, sticky=(tk.E, tk.S))
    s_lod0_maskmap_texture_path = tk.StringVar()
    entry_lod0_maskmap_texture_path = ttk.Entry(
        frame, textvariable=s_lod0_maskmap_texture_path, width=50)
    entry_lod0_maskmap_texture_path.grid(
        row=5, column=3, sticky=tk.S, pady=2, padx=2)
    button_lod0_maskmap_texture = ttk.Button(
        frame, text=u"参照",
        command=button_lod0_maskmap_texture_select_ckicked)
    button_lod0_maskmap_texture.grid(row=5, column=4, sticky=tk.S)

    label_lod0_normal_texture = ttk.Label(
        frame, text="* Normal texture", padding=(5, 2, 2, 2))
    label_lod0_normal_texture.grid(row=6, column=2, sticky=(tk.E, tk.S))
    s_lod0_normal_texture_path = tk.StringVar()
    entry_lod0_normal_texture_path = ttk.Entry(
        frame, textvariable=s_lod0_normal_texture_path, width=50)
    entry_lod0_normal_texture_path.grid(
        row=6, column=3, sticky=tk.S, pady=2, padx=2)
    button_lod0_normal_texture = ttk.Button(
        frame, text=u"参照",
        command=button_lod0_normal_texture_select_ckicked)
    button_lod0_normal_texture.grid(row=6, column=4, sticky=tk.S)

    label_lod0_micronormal_texture = ttk.Label(
        frame, text="MicroNormal texture", padding=(5, 2, 2, 2))
    label_lod0_micronormal_texture.grid(row=7, column=2, sticky=(tk.E, tk.S))
    s_lod0_micronormal_texture_path = tk.StringVar()
    entry_lod0_micronormal_texture_path = ttk.Entry(
        frame, textvariable=s_lod0_micronormal_texture_path, width=50)
    entry_lod0_micronormal_texture_path.grid(
        row=7, column=3, sticky=tk.S, pady=2, padx=2)
    button_lod0_micronormal_texture = ttk.Button(
        frame, text=u"参照",
        command=button_lod0_micronormal_texture_select_ckicked)
    button_lod0_micronormal_texture.grid(row=7, column=4, sticky=tk.S)

    label_lod0_height_texture = ttk.Label(
        frame, text="Height texture", padding=(5, 2, 2, 2))
    label_lod0_height_texture.grid(row=8, column=2, sticky=(tk.E, tk.S))
    s_lod0_height_texture_path = tk.StringVar()
    entry_lod0_height_texture_path = ttk.Entry(
        frame, textvariable=s_lod0_height_texture_path, width=50)
    entry_lod0_height_texture_path.grid(
        row=8, column=3, sticky=tk.S, pady=2, padx=2)
    button_lod0_height_texture = ttk.Button(
        frame, text=u"参照",
        command=button_lod0_height_texture_select_ckicked)
    button_lod0_height_texture.grid(row=8, column=4, sticky=tk.S)

    d_lod0_max_frontal = tk.DoubleVar(value=0.01)
    label_lod0_max_frontal = ttk.Label(
        frame, text="max frontal", padding=(5, 2, 2, 2))
    label_lod0_max_frontal.grid(row=9, column=2, sticky=(tk.S, tk.E))
    scale_lod0_max_frontal = ttk.Scale(
        frame, orient=tk.HORIZONTAL, from_=0.0, to=1.0,
        variable=d_lod0_max_frontal)
    scale_lod0_max_frontal.grid(row=9, column=3, sticky=(tk.E, tk.W, tk.S))
    entry_lod0_max_frontal = ttk.Entry(
        frame, textvariable=d_lod0_max_frontal, validate="all",
        validatecommand=(frame.register(validate_value_01), "%P"))
    entry_lod0_max_frontal.grid(row=9, column=4, sticky=(tk.E, tk.W, tk.S))

    d_lod0_max_rear = tk.DoubleVar(value=0.01)
    label_lod0_max_rear = ttk.Label(
        frame, text="max rear", padding=(5, 2, 2, 2))
    label_lod0_max_rear.grid(row=10, column=2, sticky=(tk.S, tk.E))
    scale_lod0_max_rear = ttk.Scale(
        frame, orient=tk.HORIZONTAL, from_=0.0, to=1.0,
        variable=d_lod0_max_rear)
    scale_lod0_max_rear.grid(row=10, column=3, sticky=(tk.E, tk.W, tk.S))
    entry_lod0_max_rear = ttk.Entry(
        frame, textvariable=d_lod0_max_rear, validate="all",
        validatecommand=(frame.register(validate_value_01), "%P"))
    entry_lod0_max_rear.grid(row=10, column=4, sticky=(tk.E, tk.W, tk.S))

    b_lod0_average_normals = tk.BooleanVar(value=False)
    label_lod0_average_normals = ttk.Label(
        frame, text="average normals", padding=(5, 2, 2, 2))
    label_lod0_average_normals.grid(row=11, column=2, sticky=(tk.S, tk.E))
    check_lod0_average_normals = ttk.Checkbutton(
        frame, variable=b_lod0_average_normals)
    check_lod0_average_normals.grid(row=11, column=3, sticky=(tk.W, tk.S))

    i_lod0_output_size = tk.IntVar(value=11)
    label_lod0_output_size = ttk.Label(
        frame, text="output size", padding=(5, 2, 2, 2))
    label_lod0_output_size.grid(row=12, column=2, sticky=(tk.S, tk.E))
    scale_lod0_output_size = ttk.Scale(
        frame, orient=tk.HORIZONTAL, from_=0, to=12,
        variable=i_lod0_output_size,
        command=lambda s: i_lod0_output_size.set(round(float(s))))
    scale_lod0_output_size.grid(row=12, column=3, sticky=(tk.E, tk.W, tk.S))
    vcmd = frame.register(validate_output_size), "%P"
    entry_lod0_output_size = ttk.Entry(
        frame, textvariable=i_lod0_output_size,
        validate="all", validatecommand=vcmd)
    entry_lod0_output_size.grid(row=12, column=4, sticky=(tk.E, tk.W, tk.S))

    # LOD1
    label_lod1 = ttk.Label(
        frame, text="LOD1",
        font=("", 0, "bold"),
        padding=(5, 10, 2, 2))
    label_lod1.grid(row=13, column=1, sticky=(tk.S, tk.E))

    label_lod1_fbx = ttk.Label(frame, text="fbx", padding=(5, 2, 2, 2))
    label_lod1_fbx.grid(row=13, column=2, sticky=(tk.S, tk.E))
    s_lod1_fbx_path = tk.StringVar()
    entry_lod1_fbx_path = ttk.Entry(
        frame, textvariable=s_lod1_fbx_path, width=50)
    entry_lod1_fbx_path.grid(row=13, column=3, sticky=tk.S, pady=2, padx=2)
    button_lod1_fbx = ttk.Button(
        frame, text=u"参照", command=button_lod1_fbx_select_clicked)
    button_lod1_fbx.grid(row=13, column=4, sticky=tk.S)

    d_lod1_max_frontal = tk.DoubleVar(value=0.01)
    label_lod1_max_frontal = ttk.Label(
        frame, text="max frontal", padding=(5, 2, 2, 2))
    label_lod1_max_frontal.grid(row=14, column=2, sticky=(tk.S, tk.E))
    scale_lod1_max_frontal = ttk.Scale(
        frame, orient=tk.HORIZONTAL, from_=0.0, to=1.0,
        variable=d_lod1_max_frontal)
    scale_lod1_max_frontal.grid(row=14, column=3, sticky=(tk.E, tk.W, tk.S))
    entry_lod1_max_frontal = ttk.Entry(
        frame, textvariable=d_lod1_max_frontal, validate="all",
        validatecommand=(frame.register(validate_value_01), "%P"))
    entry_lod1_max_frontal.grid(row=14, column=4, sticky=(tk.E, tk.W, tk.S))

    d_lod1_max_rear = tk.DoubleVar(value=0.01)
    label_lod1_max_rear = ttk.Label(
        frame, text="max rear", padding=(5, 2, 2, 2))
    label_lod1_max_rear.grid(row=15, column=2, sticky=(tk.S, tk.E))
    scale_lod1_max_rear = ttk.Scale(
        frame, orient=tk.HORIZONTAL, from_=0.0, to=1.0,
        variable=d_lod1_max_rear)
    scale_lod1_max_rear.grid(row=15, column=3, sticky=(tk.E, tk.W, tk.S))
    entry_lod1_max_rear = ttk.Entry(
        frame, textvariable=d_lod1_max_rear, validate="all",
        validatecommand=(frame.register(validate_value_01), "%P"))
    entry_lod1_max_rear.grid(row=15, column=4, sticky=(tk.E, tk.W, tk.S))

    b_lod1_average_normals = tk.BooleanVar(value=False)
    label_lod1_average_normals = ttk.Label(
        frame, text="average normals", padding=(5, 2, 2, 2))
    label_lod1_average_normals.grid(row=16, column=2, sticky=(tk.S, tk.E))
    check_lod1_average_normals = ttk.Checkbutton(
        frame, variable=b_lod1_average_normals)
    check_lod1_average_normals.grid(row=16, column=3, sticky=(tk.W, tk.S))

    i_lod1_output_size = tk.IntVar(value=11)
    label_lod1_output_size = ttk.Label(
        frame, text="output size", padding=(5, 2, 2, 2))
    label_lod1_output_size.grid(row=17, column=2, sticky=(tk.S, tk.E))
    scale_lod1_output_size = ttk.Scale(
        frame, orient=tk.HORIZONTAL, from_=0, to=12,
        variable=i_lod1_output_size,
        command=lambda s: i_lod1_output_size.set(round(float(s))))
    scale_lod1_output_size.grid(row=17, column=3, sticky=(tk.E, tk.W, tk.S))
    vcmd = frame.register(validate_output_size), "%P"
    entry_lod1_output_size = ttk.Entry(
        frame, textvariable=i_lod1_output_size,
        validate="all", validatecommand=vcmd)
    entry_lod1_output_size.grid(row=17, column=4, sticky=(tk.E, tk.W, tk.S))

    # LOD2
    label_lod2 = ttk.Label(
        frame, text="LOD2",
        font=("", 0, "bold"),
        padding=(5, 10, 2, 2))
    label_lod2.grid(row=18, column=1, sticky=(tk.S, tk.E))

    label_lod2_fbx = ttk.Label(frame, text="fbx", padding=(5, 2, 2, 2))
    label_lod2_fbx.grid(row=18, column=2, sticky=(tk.S, tk.E))
    s_lod2_fbx_path = tk.StringVar()
    entry_lod2_fbx_path = ttk.Entry(
        frame, textvariable=s_lod2_fbx_path, width=50)
    entry_lod2_fbx_path.grid(row=18, column=3, sticky=tk.S, pady=2, padx=2)
    button_lod2_fbx = ttk.Button(
        frame, text=u"参照", command=button_lod2_fbx_select_clicked)
    button_lod2_fbx.grid(row=18, column=4, sticky=tk.S)

    d_lod2_max_frontal = tk.DoubleVar(value=0.3)
    label_lod2_max_frontal = ttk.Label(
        frame, text="max frontal", padding=(5, 2, 2, 2))
    label_lod2_max_frontal.grid(row=19, column=2, sticky=(tk.S, tk.E))
    scale_lod2_max_frontal = ttk.Scale(
        frame, orient=tk.HORIZONTAL, from_=0.0, to=1.0,
        variable=d_lod2_max_frontal)
    scale_lod2_max_frontal.grid(row=19, column=3, sticky=(tk.E, tk.W, tk.S))
    entry_lod2_max_frontal = ttk.Entry(
        frame, textvariable=d_lod2_max_frontal, validate="all",
        validatecommand=(frame.register(validate_value_01), "%P"))
    entry_lod2_max_frontal.grid(row=19, column=4, sticky=(tk.E, tk.W, tk.S))

    d_lod2_max_rear = tk.DoubleVar(value=0.3)
    label_lod2_max_rear = ttk.Label(
        frame, text="max rear", padding=(5, 2, 2, 2))
    label_lod2_max_rear.grid(row=20, column=2, sticky=(tk.S, tk.E))
    scale_lod2_max_rear = ttk.Scale(
        frame, orient=tk.HORIZONTAL, from_=0.0, to=1.0,
        variable=d_lod2_max_rear)
    scale_lod2_max_rear.grid(row=20, column=3, sticky=(tk.E, tk.W, tk.S))
    entry_lod2_max_rear = ttk.Entry(
        frame, textvariable=d_lod2_max_rear, validate="all",
        validatecommand=(frame.register(validate_value_01), "%P"))
    entry_lod2_max_rear.grid(row=20, column=4, sticky=(tk.E, tk.W, tk.S))

    b_lod2_average_normals = tk.BooleanVar(value=False)
    label_lod2_average_normals = ttk.Label(
        frame, text="average normals", padding=(5, 2, 2, 2))
    label_lod2_average_normals.grid(row=21, column=2, sticky=(tk.S, tk.E))
    check_lod2_average_normals = ttk.Checkbutton(
        frame, variable=b_lod2_average_normals)
    check_lod2_average_normals.grid(row=21, column=3, sticky=(tk.W, tk.S))

    i_lod2_output_size = tk.IntVar(value=11)
    label_lod2_output_size = ttk.Label(
        frame, text="output size", padding=(5, 2, 2, 2))
    label_lod2_output_size.grid(row=22, column=2, sticky=(tk.S, tk.E))
    scale_lod2_output_size = ttk.Scale(
        frame, orient=tk.HORIZONTAL, from_=0, to=12,
        variable=i_lod2_output_size,
        command=lambda s: i_lod2_output_size.set(round(float(s))))
    scale_lod2_output_size.grid(row=22, column=3, sticky=(tk.E, tk.W, tk.S))
    vcmd = frame.register(validate_output_size), "%P"
    entry_lod2_output_size = ttk.Entry(
        frame, textvariable=i_lod2_output_size,
        validate="all", validatecommand=vcmd)
    entry_lod2_output_size.grid(row=22, column=4, sticky=(tk.E, tk.W, tk.S))

    # Output
    label_output = ttk.Label(
        frame, text="Output",
        font=("", 0, "bold"),
        padding=(5, 50, 5, 2))
    label_output.grid(row=23, column=1, sticky=(tk.S, tk.E))

    label_output_dir_path = ttk.Label(
        frame, text="Directory", padding=(5, 50, 2, 2))
    label_output_dir_path.grid(row=23, column=2, sticky=(tk.S, tk.E))
    s_output_dir_path = tk.StringVar()
    entry_output_dir_path = ttk.Entry(
        frame, textvariable=s_output_dir_path, width=50)
    entry_output_dir_path.grid(
        row=23, column=3, sticky=(tk.E, tk.W, tk.S), pady=2, padx=2)
    button_output_dir_path = ttk.Button(
        frame, text=u"参照", command=button_output_dir_select_clicked)
    button_output_dir_path.grid(row=23, column=4, sticky=tk.S)

    label_output_filename = ttk.Label(
        frame, text="filename", padding=(5, 2, 2, 2))
    label_output_filename.grid(row=24, column=2, sticky=(tk.E, tk.S))
    s_output_filename = tk.StringVar(value="{lod}_{textureName}.tga")
    entry_output_filename = ttk.Entry(
        frame, textvariable=s_output_filename)
    entry_output_filename.grid(
        row=24, column=3, sticky=(tk.E, tk.W, tk.S), pady=2, padx=2)

    # Bake Button
    button_frame = ttk.Frame(root)
    button_frame.grid(
        row=1, column=0, columnspan=2, sticky=(tk.N, tk.S))
    button_frame.columnconfigure(0, weight=1)
    button_frame.rowconfigure(0, weight=0)

    button_execution = ttk.Button(
        button_frame, text="Bake", padding=(10, 10),
        command=bake_button_clicked)
    button_execution.grid(pady=15, sticky=(tk.N, tk.S, tk.W, tk.E))

    # Status
    status_frame = ttk.Frame(root)
    status_frame.grid(
        row=2, column=0, columnspan=2, sticky=(tk.N, tk.E, tk.W, tk.S))
    status_frame.columnconfigure(0, weight=1)
    status_frame.rowconfigure(0, weight=1)

    status_message_tree = ttk.Treeview(
        status_frame, show='tree', height=5)
    status_message_yscroll = ttk.Scrollbar(
        status_frame, orient=tk.VERTICAL, command=status_message_tree.yview)
    status_message_tree.configure(yscrollcommand=status_message_yscroll.set)
    status_message_tree.tag_configure("error", foreground="red")
    status_message_tree.grid(row=0, column=0, sticky=(tk.N, tk.E, tk.W, tk.S))
    status_message_yscroll.grid(row=0, column=1, sticky=(tk.N, tk.S))

    status_progressbar = ttk.Progressbar(
        status_frame, orient=tk.HORIZONTAL, mode="determinate")
    status_progressbar.grid(row=1, column=0, columnspan=2, sticky=(tk.E, tk.W))

    # https://stackoverflow.com/questions/55844576/tkinter-treeview-issue-when-inserting-rows-with-tags
    def fixed_map(option):
        # Fix for setting text colour for Tkinter 8.6.9
        # From: https://core.tcl.tk/tk/info/509cafafae
        #
        # Returns the style map for 'option' with any styles starting with
        # ('!disabled', '!selected', ...) filtered out.

        # style.map() returns an empty list for missing options, so this
        # should be future-safe.
        return [elm for elm in style.map('Treeview', query_opt=option) if
                elm[:2] != ('!disabled', '!selected')]
    style = ttk.Style()
    style.map('Treeview', foreground=fixed_map(
        'foreground'), background=fixed_map('background'))

    root.mainloop()
