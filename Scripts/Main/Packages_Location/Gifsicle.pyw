from shutil import which
__GifSicle = "Gifsicle"
__GifSicle_Error_1 = "\n{1}{0}{2} not found!".format(__GifSicle, Styles.Warning, Styles.Reset)
__GifSicle_Error_2 = "\n{0}Image will not be processed.{1}{2}".format(Styles.Error, Styles.Reset, __BEL)

if system() == "Windows":
	__GifSicle = which("gifsicle")
	if __GifSicle:
		if os.path.isfile(__GifSicle):
			pass
		else:
			print(__GifSicle_Error_1 + ' {1}("{0}"){2}'.format(
				__GifSicle, Styles.Meta_Info, Styles.Reset) + __GifSicle_Error_2
			)
	else:
		print(__GifSicle_Error_1 + ' {1}("{0}"){2}'.format(
			__GifSicle, Styles.Meta_Info, Styles.Reset) + __GifSicle_Error_2
		)
else:
	try:
		if is_package_installed.get(__GifSicle.lower()):
			__GifSicle = __GifSicle.lower()
	except IndexError:
		print(__GifSicle_Error_1 + ' {1}("{0}"){2}'.format(
			__GifSicle, Styles.Meta_Info, Styles.Reset) + __GifSicle_Error_2
		)