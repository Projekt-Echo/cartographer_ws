#!/bin/zsh

# Clean up
rm -rf build install log
echo "Cleaned up"
sleep 2

# Build
colcon build
echo "Built"