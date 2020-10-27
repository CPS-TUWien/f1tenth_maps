all: \
output/plechaty1.npz \
output/berlin.npz \
output/torino_redraw_small.npz \

clean:
	rm -rf output

output/%.npz: ../maps/%.yaml
	mkdir -p output
	python3 generate-costmap.py --input=$< --output=$@ --export_images


