-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 06, 2019 at 01:03 PM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.3.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `scrapping`
--

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `title` text NOT NULL,
  `rating` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `product_url` text NOT NULL,
  `date_it` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `title`, `rating`, `description`, `product_url`, `date_it`) VALUES
(2, 'Seagate ST4000VM000 4TB 5900 RPM 64MB Cache SATA 6.0Gb/s 3.5\" Internal Hard Drive Bare Drive', '4/5', 'SATA 6Gb/s NCQ, 5900 RPM\nOptimized for high-definition consumer DVR applications\nDelivers up to 16 simultaneous streams of HD content\n24×7 operation for always-on demands DVR devices\n', 'N82E16822178378', '2019-11-06 11:28:44'),
(3, 'Seagate ST4000VM000 4TB 5900 RPM 64MB Cache SATA 6.0Gb/s 3.5\" Internal Hard Drive Bare Drive', '4/5', 'SATA 6Gb/s NCQ, 5900 RPM\nOptimized for high-definition consumer DVR applications\nDelivers up to 16 simultaneous streams of HD content\n24×7 operation for always-on demands DVR devices\n', 'N82E16822178378', '2019-11-06 11:29:52'),
(4, 'AMD RYZEN 9 3900X 12-Core 3.8 GHz (4.6 GHz Max Boost) Socket AM4 105W 100-100000023BOX Desktop Processor', '5/5', '3rd Gen Ryzen\nSocket AM4\nMax Boost Frequency 4.6 GHz\nDDR4 Support\nL2 Cache 6MB\nL3 Cache 64MB\nThermal Design Power 105W\nWith Wraith Prism cooler\n', 'N82E16819113103', '2019-11-06 11:30:41'),
(5, 'ASUS AMD AM4 ROG Strix X570-E Gaming ATX Motherboard with PCIe 4.0, WiFi 6, 2.5Gbps LAN, Dual M.2, SATA 6Gb/s, USB 3.2 Gen 2', '4/5', 'AMD AM4 socket: Ready for 2nd and 3rd Gen AMD Ryzen processors to maximize connectivity and speed with up to two M.2 Drives, USB 3.2 Gen2 and AMD StoreMI\nAura Sync RGB: ASUS-exclusive Aura Sync RGB lighting, including RGB headers and addressable Gen 2 headers\nComprehensive cooling: Active PCH heatsink, MOS heatsink with 8mm heatpipe, dual on-board M.2 heatsinks and a water pump + header\nGaming connectivity: Supports PCIe 4.0, HDMI 2.0, DisplayPort 1.2 and features dual M.2 and USB 3.2 Type-A and Type-C connectors\nGaming networking: 2.5Gbps LAN and Intel Gigabit Ethernet with ASUS LANGuard, Wi-Fi 6 (802.11 ax) with MU-MIMO, and gateway teaming via GameFirst V\n5-Way Optimization: Automated system-wide tuning, providing overclocking and cooling profiles that are tailor made for your rig\nGaming audio: High fidelity audio with SupremeFX S1220A, DTS Sound Unbound and Sonic Studio III to draw you deeper into the action\n', 'N82E16813119111', '2019-11-06 11:31:08'),
(6, 'ASUS AMD AM4 ROG Strix X570-E Gaming ATX Motherboard with PCIe 4.0, WiFi 6, 2.5Gbps LAN, Dual M.2, SATA 6Gb/s, USB 3.2 Gen 2', '4/5', 'AMD AM4 socket: Ready for 2nd and 3rd Gen AMD Ryzen processors to maximize connectivity and speed with up to two M.2 Drives, USB 3.2 Gen2 and AMD StoreMI\nAura Sync RGB: ASUS-exclusive Aura Sync RGB lighting, including RGB headers and addressable Gen 2 headers\nComprehensive cooling: Active PCH heatsink, MOS heatsink with 8mm heatpipe, dual on-board M.2 heatsinks and a water pump + header\nGaming connectivity: Supports PCIe 4.0, HDMI 2.0, DisplayPort 1.2 and features dual M.2 and USB 3.2 Type-A and Type-C connectors\nGaming networking: 2.5Gbps LAN and Intel Gigabit Ethernet with ASUS LANGuard, Wi-Fi 6 (802.11 ax) with MU-MIMO, and gateway teaming via GameFirst V\n5-Way Optimization: Automated system-wide tuning, providing overclocking and cooling profiles that are tailor made for your rig\nGaming audio: High fidelity audio with SupremeFX S1220A, DTS Sound Unbound and Sonic Studio III to draw you deeper into the action\n', 'N82E16813119111', '2019-11-06 11:38:46'),
(7, 'ASUS AMD AM4 ROG Strix X570-E Gaming ATX Motherboard with PCIe 4.0, WiFi 6, 2.5Gbps LAN, Dual M.2, SATA 6Gb/s, USB 3.2 Gen 2', '4/5', 'AMD AM4 socket: Ready for 2nd and 3rd Gen AMD Ryzen processors to maximize connectivity and speed with up to two M.2 Drives, USB 3.2 Gen2 and AMD StoreMI\nAura Sync RGB: ASUS-exclusive Aura Sync RGB lighting, including RGB headers and addressable Gen 2 headers\nComprehensive cooling: Active PCH heatsink, MOS heatsink with 8mm heatpipe, dual on-board M.2 heatsinks and a water pump + header\nGaming connectivity: Supports PCIe 4.0, HDMI 2.0, DisplayPort 1.2 and features dual M.2 and USB 3.2 Type-A and Type-C connectors\nGaming networking: 2.5Gbps LAN and Intel Gigabit Ethernet with ASUS LANGuard, Wi-Fi 6 (802.11 ax) with MU-MIMO, and gateway teaming via GameFirst V\n5-Way Optimization: Automated system-wide tuning, providing overclocking and cooling profiles that are tailor made for your rig\nGaming audio: High fidelity audio with SupremeFX S1220A, DTS Sound Unbound and Sonic Studio III to draw you deeper into the action\n', 'N82E16813119111', '2019-11-06 11:40:21');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
